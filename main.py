
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

mind_map = {}

# Creer un noeud {name, child:{}}
def create_child(name, mind_map):
    mind_map[name] = {
        'name': name,
        'child': {}
    }
    return mind_map

# Cherche et retourne un noeud
def search_child(name, mind_map):
    if name in mind_map:
        return mind_map[name]
    else:
        for elem in mind_map:
            return search_child(name, mind_map[elem]['child'])
    return False

# Supprime un noeud
def del_child(name, mind_map):
    for elem in mind_map:
        if elem == name:
            return mind_map.pop(elem)
        else:
            del_child(name, mind_map[elem]['child'])
    return False

# Ajoute un noeud sur une branche
def update_child(name, update, mind_map):
    for elem in mind_map:
        if elem == name:
            if len(mind_map[elem]['child']) == 0:
                mind_map[elem]['child'] = update
                return True
            else:
                return mind_map[elem]['child'].update(update)
        else:
            update_child(name, update, mind_map[elem]['child'])
    return False

class solveur(Resource):
    # GET (node name)
    # RETURN {}
    def get(self, name):
        if search_child(name, mind_map):
            return search_child(name, mind_map), 200
        else:
            return {
                'Error': name + ' : key does not exist'
            }, 500

    # POST (name of the new node)
    def post(self, name):
        if not search_child(name, mind_map):
            create_child(name, mind_map)
            return {
                'Message': 'Creation du Parent :' + name
            }, 201
        else:
            return {
                'Error': name + ' : key exist'
            }, 500

    # DELETE (node name)
    def delete(self, name):
        if del_child(name, mind_map):
            return {
                'Deleting': name
            }, 204
        else:
            return {
                       'Error': name + ' : key does not exist'
                   }, 500

    # PUT (node name)
    def put(self, name):
        node = create_child(request.form['child'], {})
        if search_child(name, mind_map):
            update_child(name, node, mind_map)
            return {
                'Update': name + ' add child -> ' + request.form['child']
            }, 201
        else:
            return {
                'Error': name + ' : key does not exist'
            }, 500

api.add_resource(solveur, '/<string:name>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


