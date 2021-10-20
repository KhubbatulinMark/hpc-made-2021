#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>


double random_number(unsigned int *seed) {
    return (double) rand_r(seed) * 2 / (double) (RAND_MAX) - 1;
}

double calculate_pi(int n_points) {
    double numberInCircle = 0;
	#pragma omp parallel num_threads(20)
	{
    	unsigned int seed = (unsigned int) time(NULL) + (unsigned int) omp_get_thread_num();
    	#pragma omp for reduction(+: numberInCircle)
        for (long long int i = 0; i < n_points; i++) {
            double x = random_number(&seed);
            double y = random_number(&seed);
            double distanceSquared = x*x + y*y;

            if (distanceSquared <= 1)
            	numberInCircle++;
        }
    }
    return 4 * numberInCircle/((double) n_points);
}

int main() {
    double start, end;
    int n_points = 100000000;

    start = omp_get_wtime();
    double pi = calculate_pi(n_points);
    end = omp_get_wtime();

    printf("Time: %.10f seconds \n", end - start);
    printf("π: %.10f \n", pi);

    return 0;
}