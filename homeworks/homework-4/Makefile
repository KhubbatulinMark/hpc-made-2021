SHELL = /bin/sh
CURRENT_UID := $(shell id -u)
CC=gcc-11

test_power:
	$(CC) matrix_power/matrix_pow.c -o matrix_power/matrix_pow.exe -fopenmp -O3
	./matrix_power/test_matrix_pow.sh