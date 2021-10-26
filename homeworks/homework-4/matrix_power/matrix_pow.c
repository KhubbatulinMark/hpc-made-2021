#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void random_graph(int *A, int N) {

    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            A[i * N + j] = A[i * N + j];
            if (i == j) {
                A[i * N + j] = 0;
            } else {
                A[i * N + j] = rand() & 1;
            }
        }
    }
}

void matmul(const int *A, const int *B, int *C, int N) {
    int i, j, k, offset_i, offset_k;

    for (i = 0; i < N * N; i++) {
        C[i] = 0;
    }

#pragma omp parallel for private(i, j, k, offset_i, offset_k) shared(A, B, C, N) default(none)
    for (k = 0; k < N; k++) {
    	offset_k = k * N;
        for (i = 0; i < N; i++) {
            offset_i = i * N;
            for (j = 0; j < N; j++) {
                C[offset_i + j] += A[offset_i + k] * B[offset_k + j];
            }
        }
    }
}

void matrix_pow(const int *A, int *C, int p, int N) {
    int i, j;
    int *B = malloc(N * N * sizeof(int));
    int *D = malloc(N * N * sizeof(int));
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            B[i * N + j] = A[i * N + j];
            if (i == j) {
                C[i * N + j] = 1;
            } else {
                C[i * N + j] = 0;
            }
        }
    }

    while (p > 0) {
        if (p % 2 > 0) {
            matmul(C, B, D, N);
        }
        for (i = 0; i < N * N; i++) {
            C[i] = D[i];

        }

        p = p / 2;
        matmul(B, B, D, N);
        for (i = 0; i < N * N; i++) {
            B[i] = D[i];
        }
    }
    free(B);
    free(D);
}


int main(int argc, const char* argv[]) {
    int N, power;
	if (argc > 1) {
		N = atoi(argv[1]);
		if (argc > 2) {
			power = atoi(argv[2]);
		}
	}

	int *A = malloc(N * N * sizeof(int));
    int *C = malloc(N * N * sizeof(int));

    for (int i = 0; i < N * N; i++) {
        C[i] = 0;
    }
    random_graph(A, N);

    double start = omp_get_wtime();
    matrix_pow(A, C, power, N);
    double end = omp_get_wtime();
    printf("Matrix Power %i Time: %f \n", power, end - start);

    free(A);
    free(C);

    return 0;
}