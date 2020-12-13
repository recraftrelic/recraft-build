#!/bin/bash

if [ ! -d "$1" ]; then
  npx create-react-app $1 --template typescript
  cp -rv ./templates/docker/ $1/docker/
  cp -rv ./templates/nginx/ $1/nginx/
  cp -rv ./templates/gitlab/.gitlab-ci.yml $1/.gitlab-ci.yml
fi

