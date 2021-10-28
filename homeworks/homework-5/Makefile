SHELL = /bin/sh
CURRENT_UID := $(shell id -u)

export NNODES=16

build:
	DOCKER_BUILDKIT=1 docker-compose build

rebuild:
	DOCKER_BUILDKIT=1 docker-compose build --no-cache

test_friends:
	docker-compose scale mpi_head=1 mpi_node=${NNODES}
	docker-compose exec --privileged mpi_head \
	    mpirun -n ${NNODES} --allow-run-as-root --oversubscribe python source/friends.py | tee result/friends.txt
	docker-compose down

down:
	docker-compose down