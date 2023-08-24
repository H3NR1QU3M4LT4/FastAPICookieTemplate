#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

if [ -z "$1" ]; then
  echo -e "${RED}Please provide an image version argument.${NC}"
  exit 1
fi

echo -e "${GREEN}Running 'docker build' command:${NC}"
docker build --platform=linux/amd64 -f Dockerfile.fastapi -t {{cookiecutter.directory_name}}:$1 .

echo -e "${GREEN}Running 'docker run' command:${NC}"
docker run --platform=linux/amd64 -p 80:80 -d \
  -e <ENV_VAR>="your_value"
  {{cookiecutter.directory_name}}:$1