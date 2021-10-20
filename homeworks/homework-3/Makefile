SHELL = /bin/sh
CURRENT_UID := $(shell id -u)
CC=gcc-11

test_omp_bugparfor:
	$(CC) fix-bugs/omp_bugparfor.c -o fix-bugs/omp_bugparfor.exe -fopenmp
	fix-bugs/omp_bugparfor.exe > result/omp_bugparfor.txt

test_omp_bugreduction:
	$(CC) fix-bugs/omp_bugreduction.c -o fix-bugs/omp_bugreduction.exe -fopenmp
	fix-bugs/omp_bugreduction.exe > result/omp_bugreduction.txt

test_monte-carlo-pi:
	$(CC) monte-carlo-pi/main.c -o monte-carlo-pi/main.exe -fopenmp
	monte-carlo-pi/main.exe > result/monte-carlo-pi.txt