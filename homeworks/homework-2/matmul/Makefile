CC=g++

CFLAGS=-c -Wall -g -O3

all: main

main: main.o mat_matrix_lib.a
	$(CC) main.o mat_matrix_lib.a -o main.exe

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

make_matrix.o: make_matrix.cpp
	$(CC) $(CFLAGS) make_matrix.cpp

cal_mat_mul.o: cal_mat_mul.cpp
	$(CC) $(CFLAGS) cal_mat_mul.cpp

mat_matrix_lib.a: make_matrix.o cal_mat_mul.o
	ar rcs mat_matrix_lib.a make_matrix.o cal_mat_mul.o

clean:
	rm -rf *.o *.a main.exe

testing:
	./main.exe >> tests/tests.txt

testing-docker:
	./main.exe >> tests/docker-tests.txt

build:
	 docker-compose build

run-docker:
	 docker-compose run mat_matrix_test bash