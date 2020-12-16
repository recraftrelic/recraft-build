#!/bin/bash

touch docker-compose.yml

cat <<EOT >> docker-compose.yml
version: '3'

services:
    ${1}-app:
        container_name: ${1}-app
        build:
            context: ..
            dockerfile: ./docker/Dockerfile
        volumes:
            - .:/app
            - /app/node_modules
        ports:
            - ${2}:80
EOT

cp -v docker-compose.yml $1/docker/docker-compose.yml
rm -v docker-compose.yml