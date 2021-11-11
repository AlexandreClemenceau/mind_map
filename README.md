# mind_map

Deployer : ./deploy.sh

add node : curl http://0.0.0.0:5000/<node_name> -X POST
del node : curl http://0.0.0.0:5000/<node_name> -X delete
get node : curl http://0.0.0.0:5000/<node_name>
update node : curl http://0.0.0.0:5000/<node_name> -d "child=<child_node_name>" -X PUT

Test unitaire disponible dans unit_test.py
