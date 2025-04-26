===>📄 Docker Compose Instructions (task-163)
Create a new folder with the name task-163, and inside it create a new Docker Compose file with the filename docker-compose.yml.

Add the following services and networks to the docker-compose.yml file:

Service Name | Image | Environment Variables | Ports | Networks
pod10web | wordpress:6.0 | WORDPRESS_DB_HOST=pod10dbWORDPRESS_DB_USER=rootWORDPRESS_DB_PASSWORD=task163 | 1080:80 | pod10frontend, pod10backend
pod10db | mysql:5.7 | MYSQL_ROOT_PASSWORD=task163MYSQL_DATABASE=wordpress | (none) | pod10backend
pod10test | wbitt/network-multitool | (none) | (none) | pod10frontend

(.vdocker) sushil@sushil:~/DOCKER/task-163$ cat docker-compose.yml 
services:
  pod10web:
    image: wordpress:6.0
    environment:
      - WORDPRESS_DB_HOST=pod10db
      - WORDPRESS_DB_USER=root
      - WORDPRESS_DB_PASSWORD=task163
    ports:
      - 1080:80
    networks:
      - pod10frontend
      - pod10backend 
  pod10db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: task163
      MYSQL_DATABASE: wordpress
    networks:
      - pod10backend
  pod10test:
    image: wbitt/network-multitool
    networks:
      - pod10frontend

networks:
  pod10frontend:
  pod10backend:


===>Verify that the Wordpress web service is running by browsing to http://127.0.0.1:1080
(.vdocker) sushil@sushil:~/DOCKER/task-163$ curl http://localhost:1080


===>Verify that two networks were created by using the command "docker network Is".
Inspect both of the task163 -* networks and verify which containers are connected to each of them.

(.vdocker) sushil@sushil:~/DOCKER$ docker network ls
NETWORK ID     NAME                     DRIVER    SCOPE
733ccfffee50   appnet                   bridge    local
c392d121b429   bridge                   bridge    local
d1d088021154   host                     host      local
2fea03d2a2b6   none                     null      local
b32c04972c0b   plantuml_default         bridge    local
8d3f3b659bf8   task161                  bridge    local
d35faf091a29   task162                  bridge    local
428d2ffe50f4   task-163_pod10backend    bridge    local
bfed006745d8   task-163_pod10frontend   bridge    local
59d4e539b3ef   ubuntu_app_default       bridge    local
ed89f22bc84f   ubuntu_app_net1          bridge    local
2fbde5d60903   ubuntu_app_net2          bridge    local
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task-163_pod10backend 
[
    {
        "Name": "task-163_pod10backend",
        "Id": "428d2ffe50f42f35696eaea36bb7a01dae5a9de603eba8d95f1b341dc5ca16cd",
        "Created": "2025-04-27T01:47:20.876762244+10:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.23.0.0/16",
                    "Gateway": "172.23.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "756c5b53a981380cbc86dcf01abcb0e19ba6ad78259202ec862df1e7f8de172e": {
                "Name": "task-163-pod10web-1",
                "EndpointID": "f95e512f7e1e0c9fadff25efa10376d6df0c1d26a82b9d23d4bcc18d01028b42",
                "MacAddress": "02:42:ac:17:00:03",
                "IPv4Address": "172.23.0.3/16",
                "IPv6Address": ""
            },
            "d2ad71948759916b9777813c9aab31d99f65726eee380c5815a33f241275d3c5": {
                "Name": "task-163-pod10db-1",
                "EndpointID": "de30f685a7756d0963fdabe820a183a3d81c46b722651525fad5c8e46c08ab09",
                "MacAddress": "02:42:ac:17:00:02",
                "IPv4Address": "172.23.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.config-hash": "e3f98d7334a0e30c177ab0a780302d020411a1e0576363b2f2376a701cdd2f42",
            "com.docker.compose.network": "pod10backend",
            "com.docker.compose.project": "task-163",
            "com.docker.compose.version": "2.35.1"
        }
    }
]
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task-163_pod10backend | jq '[0].Containers'
jq: error (at <stdin>:50): Cannot index array with string "Containers"
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task-163_pod10backend | jq '.[0].Containers'
{
  "756c5b53a981380cbc86dcf01abcb0e19ba6ad78259202ec862df1e7f8de172e": {
    "Name": "task-163-pod10web-1",
    "EndpointID": "f95e512f7e1e0c9fadff25efa10376d6df0c1d26a82b9d23d4bcc18d01028b42",
    "MacAddress": "02:42:ac:17:00:03",
    "IPv4Address": "172.23.0.3/16",
    "IPv6Address": ""
  },
  "d2ad71948759916b9777813c9aab31d99f65726eee380c5815a33f241275d3c5": {
    "Name": "task-163-pod10db-1",
    "EndpointID": "de30f685a7756d0963fdabe820a183a3d81c46b722651525fad5c8e46c08ab09",
    "MacAddress": "02:42:ac:17:00:02",
    "IPv4Address": "172.23.0.2/16",
    "IPv6Address": ""
  }
}
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task-163_pod10frontend | jq '.[0].Containers'
{
  "756c5b53a981380cbc86dcf01abcb0e19ba6ad78259202ec862df1e7f8de172e": {
    "Name": "task-163-pod10web-1",
    "EndpointID": "899b707e49e31f7efea0e16f116c59d00f9f6bed3493a29f9c375a25033510a4",
    "MacAddress": "02:42:ac:15:00:03",
    "IPv4Address": "172.21.0.3/16",
    "IPv6Address": ""
  },
  "cc9d1df95aa89e30a83d3cf77134dc0afa1b3fd2ae273ae7309ec426e4ade6ea": {
    "Name": "task-163-pod10test-1",
    "EndpointID": "a6f131e152de6598b12fa87895b5053f7e51a17190035dbafbd5bacd7ca51333",
    "MacAddress": "02:42:ac:15:00:02",
    "IPv4Address": "172.21.0.2/16",
    "IPv6Address": ""
  }
}

🎯 Official requirements from your image:
Named Volume | Host Path      | Destination Path | Service Name | Access Mode
pod10db-data | (named volume) | /var/lib/mysql   | pod10db   | Read and write
                test.txt      | /var/test.txt    | pod10test | Read-only

services:
  pod10web:
    image: wordpress:6.0
    environment:
      - WORDPRESS_DB_HOST=pod10db
      - WORDPRESS_DB_USER=root
      - WORDPRESS_DB_PASSWORD=task163
    ports:
      - 1080:80
    networks:
      - pod10frontend
      - pod10backend

  pod10db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: task163
      MYSQL_DATABASE: wordpress
    networks:
      - pod10backend
    volumes:
      - pod10db-data:/var/lib/mysql

  pod10test:
    image: wbitt/network-multitool
    networks:
      - pod10frontend
    volumes:
      - ./test.txt:/var/test.txt:ro

networks:
  pod10frontend:
  pod10backend:

volumes:
  pod10db-data:


===>📄 Verify Volume Mount for task163_pod10db
Verify with docker inspect that your task163_pod10db container has the correct volume mounted in rw (read-write) mode.

(.vdocker) sushil@sushil:~/DOCKER/task-163$ docker inspect task-163-pod10db-1 | jq '.[0].Mounts'
[
  {
    "Type": "volume",
    "Name": "task-163_pod10db-data",
    "Source": "/var/lib/docker/volumes/task-163_pod10db-data/_data",
    "Destination": "/var/lib/mysql",
    "Driver": "local",
    "Mode": "rw",
    "RW": true,
    "Propagation": ""
  }
]

===>Verify the host-mapped file by entering pod10test's bash shell using the command "docker exec -it
task163_pod10test_1 bash" and cat /var/test.txt

(.vdocker) sushil@sushil:~/DOCKER/task-163$ docker exec -it task-163-pod10test-1 bash
c270a1ab9f05:/var# ls -la
total 68
drwxr-xr-x    1 root     root          4096 Apr 26 16:16 .
drwxr-xr-x    1 root     root          4096 Apr 26 16:16 ..
drwxr-xr-x    1 root     root          4096 Aug  7  2023 cache
dr-xr-xr-x    2 root     root          4096 Aug  7  2023 empty
drwxr-xr-x    1 root     root          4096 Sep 14  2023 lib
drwxr-xr-x    2 root     root          4096 Aug  7  2023 local
drwxr-xr-x    3 root     root          4096 Aug  7  2023 lock
drwxr-xr-x    1 root     root          4096 Sep 14  2023 log
drwxr-xr-x    2 root     root          4096 Aug  7  2023 mail
drwxr-xr-x    2 root     root          4096 Aug  7  2023 opt
lrwxrwxrwx    1 root     root             4 Aug  7  2023 run -> /run
drwxr-xr-x    3 root     root          4096 Aug  7  2023 spool
-rw-rw-r--    1 999      1000            17 Apr 26 16:05 test.txt
drwxrwxrwt    2 root     root          4096 Aug  7  2023 tmp
drwxr-xr-x    3 root     root          4096 Sep 14  2023 www
c270a1ab9f05:/var# cat test.txt 
Welcome to pod10
c270a1ab9f05:/var# echo "Trying to change the ro text.txt file" > test.txt 
bash: test.txt: Read-only file system
c270a1ab9f05:/var# 