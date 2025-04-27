# 📄 Docker Compose Instructions (task-163)

---

## 📁 Create a New Folder and File
- Create a new folder with the name `task-163`.
- Inside it create a new Docker Compose file with the filename `docker-compose.yml`.

---

## 🛠️ Add the Following Services and Networks

| **Service Name** | **Image** | **Environment Variables** | **Ports** | **Networks** |
|:-----------------|:----------|:---------------------------|:---------|:-------------|
| pod10web | wordpress:6.0 | WORDPRESS_DB_HOST=pod10db, WORDPRESS_DB_USER=root, WORDPRESS_DB_PASSWORD=task163 | 1080:80 | pod10frontend, pod10backend |
| pod10db | mysql:5.7 | MYSQL_ROOT_PASSWORD=task163, MYSQL_DATABASE=wordpress | (none) | pod10backend |
| pod10test | wbitt/network-multitool | (none) | (none) | pod10frontend |

---

## 📄 docker-compose.yml content

```yaml
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
```

---

## ✅ Verify Wordpress Web Service
```bash
(.vdocker) sushil@sushil:~/DOCKER/task-163$ curl http://localhost:1080
```

---

## ✅ Verify Networks Created
```bash
(.vdocker) sushil@sushil:~/DOCKER$ docker network ls
```

Sample Output:
```bash
NETWORK ID     NAME                     DRIVER    SCOPE
...
428d2ffe50f4   task-163_pod10backend    bridge    local
bfed006745d8   task-163_pod10frontend   bridge    local
...
```

---

## ✅ Inspect Networks and Attached Containers

Inspect `task-163_pod10backend`:
```bash
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task-163_pod10backend | jq '.[0].Containers'
```

Sample Output:
```json
{
  "756c5b53a981380cbc86dcf01abcb0e19ba6ad78259202ec862df1e7f8de172e": {
    "Name": "task-163-pod10web-1",
    "IPv4Address": "172.23.0.3/16"
  },
  "d2ad71948759916b9777813c9aab31d99f65726eee380c5815a33f241275d3c5": {
    "Name": "task-163-pod10db-1",
    "IPv4Address": "172.23.0.2/16"
  }
}
```

Inspect `task-163_pod10frontend`:
```bash
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task-163_pod10frontend | jq '.[0].Containers'
```

Sample Output:
```json
{
  "756c5b53a981380cbc86dcf01abcb0e19ba6ad78259202ec862df1e7f8de172e": {
    "Name": "task-163-pod10web-1",
    "IPv4Address": "172.21.0.3/16"
  },
  "cc9d1df95aa89e30a83d3cf77134dc0afa1b3fd2ae273ae7309ec426e4ade6ea": {
    "Name": "task-163-pod10test-1",
    "IPv4Address": "172.21.0.2/16"
  }
}
```

---

## 📦 Official Volume Requirements

| **Named Volume** | **Host Path** | **Destination Path** | **Service Name** | **Access Mode** |
|:-----------------|:--------------|:---------------------|:-----------------|:----------------|
| pod10db-data | (named volume) | /var/lib/mysql | pod10db | Read and Write |
| test.txt | ./test.txt | /var/test.txt | pod10test | Read-only |

---

## 🔍 Verify Volume Mount for pod10db

```bash
(.vdocker) sushil@sushil:~/DOCKER/task-163$ docker inspect task-163-pod10db-1 | jq '.[0].Mounts'
```

Sample Output:
```json
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
```

---

## 🔦 Verify the Host-Mapped File inside pod10test

1. Enter the bash shell:
```bash
(.vdocker) sushil@sushil:~/DOCKER/task-163$ docker exec -it task-163-pod10test-1 bash
```

2. Inside container, check `/var/test.txt`:
```bash
c270a1ab9f05:/var# ls -la
```

Check Content:
```bash
c270a1ab9f05:/var# cat test.txt
Welcome to pod10
```

3. Attempt to Modify (should fail, as expected read-only):
```bash
c270a1ab9f05:/var# echo "Trying to change the ro text.txt file" > test.txt
bash: test.txt: Read-only file system
```

---

# 🎯 Task Completed Successfully!

---

