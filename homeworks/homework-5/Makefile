SHELL = /bin/sh
CURRENT_UID := $(shell id -u)

export NNODES=16

build:
	DOCKER_BUILDKIT=1 docker-compose build

rebuild:
	DOCKER_BUILDKIT=1 docker-compose build --no-cache

test_friends:
	docker-compose up -d --scale mpi_node=${NNODES}
	docker-compose exec --privileged mpi_head \
	    mpirun -n ${NNODES} --allow-run-as-root --oversubscribe python source/friends.py | tee result/friends.txt
	docker-compose down

test_war_and_peace:
	docker-compose up -d --scale mpi_node=${NNODES}
	docker-compose exec --privileged mpi_head \
	    mpirun -n ${NNODES} --allow-run-as-root --oversubscribe python source/war_and_peace.py | tee result/war_and_peace.txt
	docker-compose down


down:
	docker-compose down