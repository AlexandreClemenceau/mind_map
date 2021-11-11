docker stop mind_map
docker build -t mind_map:v1 .
docker run -dit --rm -p 5000:5000 --name mind_map mind_map:v1