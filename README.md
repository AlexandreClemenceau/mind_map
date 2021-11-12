# mind_map
Necessite Docker et Git

Deployer : ./deploy.sh

add node : curl http://localhost:5000/<node_name> -X POST

del node : curl http://localhost:5000/<node_name> -X delete

get node : curl http://localhost:5000/<node_name>

update node : curl http://localhost:5000/<node_name> -d "child=<child_node_name>" -X PUT

Test unitaire disponible dans unit_test.py
