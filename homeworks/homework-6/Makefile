SHELL = /bin/sh
CURRENT_UID := $(shell id -u)

build:
	DOCKER_BUILDKIT=1 docker-compose build

rebuild:
	DOCKER_BUILDKIT=1 docker-compose build --no-cache

up:
	DOCKER_BUILDKIT=1 docker-compose up -d --force-recreate

down:
	docker-compose down