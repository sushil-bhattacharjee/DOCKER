#!/bin/bash

DOCKER_ID=$(docker run -d -p 9500:9500 app2)
sleep 3

python3 app2_tests.py
EXIT_CODE=$?

docker kill $DOCKER_ID
docker rm $DOCKER_ID
exit $EXIT_CODE