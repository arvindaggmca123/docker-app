1) docker volume create db-data
2) docker volume create nginxconf
3) docker network create test_network
4)open "command prompt" at current location, where we have docker-compose.yml file

5)run the bellow command on command prompt:
-> docker-compose up
6)check docker container using command => sudo docker ps
7)enter mongodb container using command => sudo docker exec -it containerid /bin/bash
8)start mongodb using command => mongod
9)create database using command => use samples
10)create collection using command =>db.createCollection("samples")
11) hit the bellow url:
-> http://localhost:5001    (without nginx reverse proxy server,directly hit request on python server)
-> http://localhost         (with nginx reverse proxy,hit request through nginx)
