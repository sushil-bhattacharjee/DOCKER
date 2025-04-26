<!-- markdownlint-disable -->


🧠 Just run a container 
Pick a docker container name from the https://hub.docker.com/search?q=http

(.vdocker) sushil@sushil:~/DOCKER$ docker run httpd
Unable to find image 'httpd:latest' locally
latest: Pulling from library/httpd
8a628cdd7ccc: Pull complete 
60ba3d18ad64: Pull complete 
4f4fb700ef54: Pull complete 
03e322382f93: Pull complete 
4ad6b63c403f: Pull complete 
c613327bbca6: Pull complete 
Digest: sha256:4564ca7604957765bd2598e14134a1c6812067f0daddd7dc5a484431dd03832b
Status: Downloaded newer image for httpd:latest
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
[Wed Apr 23 14:49:33.442195 2025] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.63 (Unix) configured -- resuming normal operations
[Wed Apr 23 14:49:33.442312 2025] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
172.17.0.1 - - [23/Apr/2025:14:50:21 +0000] "GET / HTTP/1.1" 200 45
172.17.0.1 - - [23/Apr/2025:14:50:21 +0000] "GET /favicon.ico HTTP/1.1" 404 196
^C[Wed Apr 23 14:51:06.222106 2025] [core:warn] [pid 1:tid 1] AH00045: child process 11 still did not exit, sending a SIGTERM
^Z[Wed Apr 23 14:51:08.222768 2025] [core:warn] [pid 1:tid 1] AH00045: child process 11 still did not exit, sending a SIGTERM
172.17.0.1 - - [23/Apr/2025:14:51:09 +0000] "-" 408 -

🧠 Run a container with specific port to access from Outside
(.vdocker) sushil@sushil:~/DOCKER$ sudo docker run -p 8081:80 httpd
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
[Wed Apr 23 14:55:56.114150 2025] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.63 (Unix) configured -- resuming normal operations
[Wed Apr 23 14:55:56.114251 2025] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'(.vdocker) sushil@sushil:~/DOCKER$ sudo docker run -p 80:80 httpd

***8081 is the outside port that can reach the server. http://<host-ip>:8081

###List the running containers | "ps" stands for "process status"
(.vdocker) sushil@sushil:~/DOCKER$ docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED        STATUS      PORTS                       NAMES
23a6705b1534   plantuml/plantuml-server:tomcat   "/entrypoint.sh cata…"   3 months ago   Up 3 days   10.1.10.98:9180->8080/tcp   plantuml_server

--->$ watch docker ps
Every 2.0s: docker ps                                                                                                                                          sushil: Thu Apr 24 01:06:14 2025

CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS          PORTS                                   NAMES
48ea23f8fd15   httpd                             "httpd-foreground"       18 seconds ago   Up 17 seconds   0.0.0.0:8081->80/tcp, :::8081->80/tcp   upbeat_kowalevski
23a6705b1534   plantuml/plantuml-server:tomcat   "/entrypoint.sh cata…"   3 months ago     Up 3 days       10.1.10.
98:9180->8080/tcp               plantuml_server

--->> Check the IP block used by docker
(.vdocker) sushil@sushil:~/DOCKER$ ip a

 docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:0a:f7:91:bc brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:aff:fef7:91bc/64 scope link 
       valid_lft forever preferred_lft forever

---> Check the docker network ls | by default the container run from the bridge
(.vdocker) sushil@sushil:~/DOCKER$ docker network ls
NETWORK ID     NAME               DRIVER    SCOPE
733ccfffee50   appnet             bridge    local
8f1b8c030a98   bridge             bridge    local
d1d088021154   host               host      local
2fea03d2a2b6   none               null      local
b32c04972c0b   plantuml_default   bridge    local

---> Inspect the bridge that docker container is using
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect bridge
[
    {
        "Name": "bridge",
        "Id": "8f1b8c030a98fb5bd7c93966f0da23048c82f4b544788a7b81c918b700956a33",
        "Created": "2025-04-20T18:39:53.04167357+10:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
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
            "f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21": {
                "Name": "gracious_cori",
                "EndpointID": "69f7ed00572949fabce5cc2e143279c90945b3179c25344287a31aa0e54e991e",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]

---> Inspect particular docker container
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect f47d3cf9be11
[
    {
        "Id": "f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21",
        "Created": "2025-04-23T15:12:40.298364581Z",
        "Path": "httpd-foreground",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 4149793,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2025-04-23T15:12:40.494381864Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:10fd72f437c47dfdf71c3c5824ebc07d3fb4544bd074e8ce6b79f5eb3fc211a9",
        "ResolvConfPath": "/var/lib/docker/containers/f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21/hostname",
        "HostsPath": "/var/lib/docker/containers/f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21/hosts",
        "LogPath": "/var/lib/docker/containers/f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21/f47d3cf9be11c748dc695ef635b7ec50133fee9c12f4f87733b5d7dfb6ea1e21-json.log",
        "Name": "/gracious_cori",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8083"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                41,
                191
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/1beca2c8e3c539201843643d71d5faadc341838a4afec895db01f698b80e5639-init/diff:/var/lib/docker/overlay2/79eeab4b17ce21ec7238c1f0005d8d1014985bea05e5cfa91369d92e0070c0b2/diff:/var/lib/docker/overlay2/745cddc5a7c4bf43ec1c729a436fd40855ffa18df619644fe1065d618438498e/diff:/var/lib/docker/overlay2/6b4b49307cf885ba8e256563eb28197d94ba907e891679ff5014bc16e0ee51c0/diff:/var/lib/docker/overlay2/96765da351981eca650425cd302e4d6171f56c23f585b1bc0f13f0a246d06f30/diff:/var/lib/docker/overlay2/093d38c30f643c78812283c5689414f33158016e3251f7ca313d7afec18ec8bc/diff:/var/lib/docker/overlay2/49cc9ee6f5d95038f4e04ed3661a2f2a4a83cca7654bae0508d2c162c4d55009/diff",
                "MergedDir": "/var/lib/docker/overlay2/1beca2c8e3c539201843643d71d5faadc341838a4afec895db01f698b80e5639/merged",
                "UpperDir": "/var/lib/docker/overlay2/1beca2c8e3c539201843643d71d5faadc341838a4afec895db01f698b80e5639/diff",
                "WorkDir": "/var/lib/docker/overlay2/1beca2c8e3c539201843643d71d5faadc341838a4afec895db01f698b80e5639/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f47d3cf9be11",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/apache2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "HTTPD_PREFIX=/usr/local/apache2",
                "HTTPD_VERSION=2.4.63",
                "HTTPD_SHA256=88fc236ab99b2864b248de7d49a008ec2afd7551e64dce8b95f58f32f94c46ab",
                "HTTPD_PATCHES="
            ],
            "Cmd": [
                "httpd-foreground"
            ],
            "Image": "httpd",
            "Volumes": null,
            "WorkingDir": "/usr/local/apache2",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {},
            "StopSignal": "SIGWINCH"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "3e12bcff4bba7ba5ddc9568e0708dacac50145f76a905633fc6f80ba74d2a2ba",
            "SandboxKey": "/var/run/docker/netns/3e12bcff4bba",
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8083"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "8083"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "69f7ed00572949fabce5cc2e143279c90945b3179c25344287a31aa0e54e991e",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "02:42:ac:11:00:02",
                    "NetworkID": "8f1b8c030a98fb5bd7c93966f0da23048c82f4b544788a7b81c918b700956a33",
                    "EndpointID": "69f7ed00572949fabce5cc2e143279c90945b3179c25344287a31aa0e54e991e",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DriverOpts": null,
                    "DNSNames": null
                }
            }
        }
    }
]

--->> Run a specific version of image | find the tag value from the docker hub website
https://hub.docker.com/_/httpd/tags

(.vdocker) sushil@sushil:~/DOCKER$ sudo docker run -p 8083:80 httpd:2.4.62

---> Excuting the direct command to the container
.vdocker) sushil@sushil:~/DOCKER$ docker exec -it 047579f507f4 pwd
/usr/local/apache2


---> Change the content inside the container | once you restarted, container will start from the scratch.

http://172.17.0.1:8083/demo.html

(.vdocker) sushil@sushil:~/DOCKER$ docker exec -it 047579f507f4 bash
root@047579f507f4:/usr/local/apache2# ls -la
total 56
drwxr-xr-x 1 www-data www-data 4096 Jan 14 02:21 .
drwxr-xr-x 1 root     root     4096 Jan 14 02:19 ..
drwxr-xr-x 2 root     root     4096 Jan 14 02:21 bin
drwxr-xr-x 2 root     root     4096 Jan 14 02:21 build
drwxr-xr-x 2 root     root     4096 Jan 14 02:21 cgi-bin
drwxr-xr-x 4 root     root     4096 Jan 14 02:21 conf
drwxr-xr-x 3 root     root     4096 Jan 14 02:21 error
drwxr-xr-x 2 root     root     4096 Jan 14 02:21 htdocs
drwxr-xr-x 3 root     root     4096 Jan 14 02:21 icons
drwxr-xr-x 2 root     root     4096 Jan 14 02:21 include
drwxr-xr-x 1 root     root     4096 Apr 23 15:34 logs
drwxr-xr-x 2 root     root     4096 Jan 14 02:21 modules
root@047579f507f4:/usr/local/apache2# cd htdocs/
root@047579f507f4:/usr/local/apache2/htdocs# ls
index.html
root@047579f507f4:/usr/local/apache2/htdocs# cat index.html 
<html><body><h1>It works!</h1></body></html>
root@047579f507f4:/usr/local/apache2/htdocs# vi index.html 
bash: vi: command not found
root@047579f507f4:/usr/local/apache2/htdocs# echo "<h1>Wecome to James Bond World</h1>" > demo.html
root@047579f507f4:/usr/local/apache2/htdocs# ls
demo.html  index.html


---> add a volume inside the container | Change the container content and restart to check the change stays there | 
To keep the changed content persistance; then it is required to mount a volume [a storage and file systems from the PC]

(.vdocker) sushil@sushil:~/DOCKER$ sudo docker run -p 8083:80 -v DEMO_VOL:/usr/local/apache2/htdocs httpd:2.4.62

(.vdocker) sushil@sushil:~/DOCKER$ docker inspect 3d7749cf6f75
 "Mounts": [
            {
                "Type": "volume",
                "Name": "DEMO_VOL",
                "Source": "/var/lib/docker/volumes/DEMO_VOL/_data",
                "Destination": "/usr/local/apache2/htdocs",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""

---> Mounting local volume and filesystem | absolute path
(.vdocker) sushil@sushil:~/DOCKER$ sudo docker run -p 8083:80 -v /home/sushil/DOCKER:/usr/local/apache2/htdocs httpd:2.4.62
(.vdocker) sushil@sushil:~/DOCKER$ touch local_file_demo.html
(.vdocker) sushil@sushil:~/DOCKER$ pwd
/home/sushil/DOCKER
(.vdocker) sushil@sushil:~/DOCKER$ ls
app  app2  db  DB2  docker-command.md  docker-compose.yml  info.text  lb  LB2  local_file_demo.html  outside_int_docker_routing.text  README.md  tests2
(.vdocker) sushil@sushil:~/DOCKER$ cat local_file_demo.html 
<h1>Welcome to hiTech</h1>

(.vdocker) sushil@sushil:~/DOCKER$ docker inspect 6b81d7ff06ea
 "Mounts": [
            {
                "Type": "bind",
                "Source": "/home/sushil/DOCKER",
                "Destination": "/usr/local/apache2/htdocs",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"


---> Mounting local volume | relative path
(.vdocker) sushil@sushil:~$ sudo docker run -p 8083:80 -v "$PWD/DOCKER:/usr/local/apache2/htdocs" httpd:2.4.62

---> Creating a docker image 
(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker build . -t flask
(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker image ls                                                                                              
REPOSITORY                             TAG       IMAGE ID       CREATED          SIZE
flask                                  latest    7d5368742087   30 seconds ago   488MB
httpd                                  latest    10fd72f437c4   3 months ago     148MB
app2                                   v1        c8147fea39db   3 months ago     1.03GB

---> run the docker image
(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker run -p 5000:5000 flask

---> list of docker images
(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker rmi flask
Error response from daemon: conflict: unable to remove repository reference "flask" (must force) - container 12c7e9fe9654 is using its referenced image 7d5368742087

***The error is because a stopped container (12c7e9fe9654) is still using the image flask. You need to remove the container before removing the image.

(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker ps -a
CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS                       PORTS                                               NAMES
12c7e9fe9654   flask                             "/bin/sh -c 'python3…"   24 minutes ago   Exited (137) 2 minutes ago                                                       romantic_goldstine

(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker image ls
REPOSITORY                             TAG       IMAGE ID       CREATED          SIZE
flask                                  latest    7d5368742087   26 minutes ago   488MB

(.vdocker) sushil@sushil:~/DOCKER/ubuntu_app$ docker rm 12c7e9fe9654
12c7e9fe9654

---> using the docker CLI, crate a new network with name "task161"
(.vdocker) sushil@sushil:~/DOCKER$ docker network create task161
8d3f3b659bf87d960628f3f9bd2047241d15d4502fa6018cb990869bf83a1c9d

---> use the "docker network ls" to find the network ID of task161
(.vdocker) sushil@sushil:~/DOCKER$ docker network ls
NETWORK ID     NAME               DRIVER    SCOPE
733ccfffee50   appnet             bridge    local
c392d121b429   bridge             bridge    local
d1d088021154   host               host      local
2fea03d2a2b6   none               null      local
b32c04972c0b   plantuml_default   bridge    local
8d3f3b659bf8   task161            bridge    local

===> Which dubnet was assigned to the task161 network?
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect 8d3
[
    {
        "Name": "task161",
        "Id": "8d3f3b659bf87d960628f3f9bd2047241d15d4502fa6018cb990869bf83a1c9d",
        "Created": "2025-04-26T00:35:52.520816513+10:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
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
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]

===> Are there any containers connected to the task161 network at the moment?
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect 8d3
[
    {
        "Name": "task161",
        "Id": "8d3f3b659bf87d960628f3f9bd2047241d15d4502fa6018cb990869bf83a1c9d",
        "Created": "2025-04-26T00:35:52.520816513+10:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
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
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect b32
[
    {
        "Name": "plantuml_default",
        "Id": "b32c04972c0b9d89f62c26319844e0565fbad587821b96bd742e4fbbc2ea199f",
        "Created": "2024-12-28T17:47:41.868174388+11:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": true,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "23a6705b15343c15231ab5c35e96d6c980fd11c5565a8c9eed987db4f7358890": {
                "Name": "plantuml_server",
                "EndpointID": "d8d9b1b042eb1bf4e208da15f8c2fd068a7d01937c6ba0307c7ad82c498f8c1c",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "default",
            "com.docker.compose.project": "plantuml",
            "com.docker.compose.version": "1.29.2"
        }
    }
]

✅ 4. Run an httpd container attached to task161, mapping port 8081 on host to port 80 in the container:
docker run -d --name web161 --network task161 -p 8081:80 httpd
-d: Run in detached mode

--name web161: Name the container (optional)

--network task161: Connect to the custom network

-p 8081:80: Map host port 8081 to container port 80

httpd: Use the Apache HTTP server image

✅ 5. Verify it’s working:
Open a browser and go to: http://127.0.0.1:8081

===>Verify that the container is indeed attached to the task161 network
(.vdocker) sushil@sushil:~/DOCKER$ docker network ls
NETWORK ID     NAME               DRIVER    SCOPE
733ccfffee50   appnet             bridge    local
c392d121b429   bridge             bridge    local
d1d088021154   host               host      local
2fea03d2a2b6   none               null      local
b32c04972c0b   plantuml_default   bridge    local
8d3f3b659bf8   task161            bridge    local

(.vdocker) sushil@sushil:~/DOCKER$ docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS          PORTS                                   NAMES
a3b38da53674   httpd                             "httpd-foreground"       6 minutes ago   Up 6 minutes    0.0.0.0:8081->80/tcp, :::8081->80/tcp   web161
23a6705b1534   plantuml/plantuml-server:tomcat   "/entrypoint.sh cata…"   3 months ago    Up 29 minutes   10.1.10.98:9180->8080/tcp               plantuml_server

(.vdocker) sushil@sushil:~/DOCKER$ docker inspect 8d3 | jq '.[0].Containers'
{
  "a3b38da5367414442d8ef17bd44d46f61621d416f8fd180ecc1f352fd6de96e4": {
    "Name": "web161",
    "EndpointID": "119f2322c55506e1a3bd82f7d1594f60652e3b1788a7d0222dc6198b3cdcb9d4",
    "MacAddress": "02:42:ac:13:00:02",
    "IPv4Address": "172.19.0.2/16",
    "IPv6Address": ""
  }
}
✅ Correct way to access .NetworkSettings.Networks:
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect a3b38da5 | jq '.[0].NetworkSettings.Networks'
{
  "task161": {
    "IPAMConfig": null,
    "Links": null,
    "Aliases": null,
    "MacAddress": "02:42:ac:13:00:02",
    "NetworkID": "8d3f3b659bf87d960628f3f9bd2047241d15d4502fa6018cb990869bf83a1c9d",
    "EndpointID": "119f2322c55506e1a3bd82f7d1594f60652e3b1788a7d0222dc6198b3cdcb9d4",
    "Gateway": "172.19.0.1",
    "IPAddress": "172.19.0.2",
    "IPPrefixLen": 16,
    "IPv6Gateway": "",
    "GlobalIPv6Address": "",
    "GlobalIPv6PrefixLen": 0,
    "DriverOpts": null,
    "DNSNames": [
      "web161",
      "a3b38da53674"
    ]
  }
}
✅ If you want to narrow it to just the task161 network details:
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect a3b38da5 | jq '.[0].NetworkSettings.Networks.task161'
{
  "IPAMConfig": null,
  "Links": null,
  "Aliases": null,
  "MacAddress": "02:42:ac:13:00:02",
  "NetworkID": "8d3f3b659bf87d960628f3f9bd2047241d15d4502fa6018cb990869bf83a1c9d",
  "EndpointID": "119f2322c55506e1a3bd82f7d1594f60652e3b1788a7d0222dc6198b3cdcb9d4",
  "Gateway": "172.19.0.1",
  "IPAddress": "172.19.0.2",
  "IPPrefixLen": 16,
  "IPv6Gateway": "",
  "GlobalIPv6Address": "",
  "GlobalIPv6PrefixLen": 0,
  "DriverOpts": null,
  "DNSNames": [
    "web161",
    "a3b38da53674"
  ]
}
(.vdocker) sushil@sushil:~/DOCKER$ 

===> Consider an enterprise network that uses RFC 1918 private addresses 10.0.0.0/8, 172.16.0.0/12 and
192.168.0.0/16. Would your container be able to communicate with hosts throughout all these ranges?

***Enter the the containers bash shell using the command
docker exec -it YourContainerId bash

***Verify that you can reach the internet by updating the APT cache using the command:
apt-get update
(.vdocker) sushil@sushil:~/DOCKER$ docker exec -it a3b38da5 bash
root@a3b38da53674:/usr/local/apache2# apt-get update
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8792 kB]
Get:5 http://deb.debian.org/debian bookworm-updates/main amd64 Packages [512 B]
Get:6 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [260 kB]
Fetched 9307 kB in 2s (6189 kB/s)                         
Reading package lists... Done

🔐 "IP Masquerading Disabled" — What it means in Docker:
IP masquerading is a form of source NAT (SNAT) that allows containers (with private IPs) to access the outside world (like the Internet) using the host’s public IP address.

When IP masquerading is disabled, it means:

The container cannot access external networks (like the internet) via the host's IP.

🧠 Think of it like this:
Feature | Masquerading Enabled ✅ | Masquerading Disabled ❌
Container accesses internet | Yes (via host’s IP) | No (unless explicit NAT or routing)
NAT from private to public IP | Happens | Doesn’t happen
Use case | Most typical container setups | Isolated/internal networks


===> Using the docker CLI, create a new network with the name "task162" with IP masquerading disabled:
(.vdocker) sushil@sushil:~/DOCKER$ docker network create task162 -o "com.docker.network.bridge.enable_ip_masquerade"="false"
d35faf091a29f5079abebda203139df97d42592dcbce71aeffeac0d7af689cf6

===> Using the docker CLI, run an instance of the httpd web server connected to the task162 network with TCP
container port 80 exposed as host port 8081, and verify that you can reach the "It works!" page through a
browser at http://127.0.0.1:8081

(.vdocker) sushil@sushil:~/DOCKER$ docker run --name web162 --network task162 -p 8081:80 httpd

===> Display the details of network task162 using docker inspect, and verify that the httpd container is attached to it and that IP masquerading is disabled.

(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task162 | jq '.[0].Containers'
{
  "e45bb828b0250e151c23f2cda781812e4c438d37610a9ada17f2092e0b275bf7": {
    "Name": "web162",
    "EndpointID": "4fcea55eaee867fa82c7017e30456ced19e2a2e9c3189ed63b2bc9dc40bd7940",
    "MacAddress": "02:42:ac:16:00:02",
    "IPv4Address": "172.22.0.2/16",
    "IPv6Address": ""
  }
}
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task162 | jq '.[0].Options'
{
  "com.docker.network.bridge.enable_ip_masquerade": "false"
}

===>Verify whether you can or can't reach the internet by updating the APT cache using the command:
(.vdocker) sushil@sushil:~/DOCKER$ docker exec -it e45bb828 bash
root@e45bb828b025:/usr/local/apache2# apt-get update
Ign:1 http://deb.debian.org/debian bookworm InRelease
Ign:2 http://deb.debian.org/debian bookworm-updates InRelease
0% [Connecting to deb.debian.org]^C
root@e45bb828b025:/usr/local/apache2#

===> Compare task161 and task162 for the "options"
(.vdocker) sushil@sushil:~/DOCKER$ docker inspect task162 | jq '.[0].Options'
{
  "com.docker.network.bridge.enable_ip_masquerade": "false"
}
(.vdocker) sushil@sushil:~/DOCKER$  docker inspect task161 | jq '.[0].Options'
{}