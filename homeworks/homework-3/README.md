# Homework #3

1.) Демонстрационные файлы – работающие примеры кодов для понимания OpenMP. Эти задания не оцениваются.
[omp_hello.c](demo-scripts/omp_hello.c) – простейшая программа печатающая ‘Hello world’. Введение в конструкцию ‘parallel’. 

Задание:

А) научитесь вручную менять кол-во нитей, исполняемых в программе путем изменения переменной окружения:
$ export OMP_NUM_THREADS=number you want.

B) научитесь задавать кол-во нитей внутри программы.
* [omp_outmes.c](demo-scripts/omp_outmes.c) – сравнение параллельного I/O C и C++. Пример на понимания понятия “threadsafe”. Пример конструкции critical. Компиляция:
$ g++ OutMes.cpp -o <executable> -fopenmp 
* [omp_privateshared.c](demo-scripts/omp_privateshared.c) – пример общих и приватных переменных, конструкции ‘for’. Задание: запустите программу, разберитесь, что делают все команды с #pragma.
* [omp_parsec.c](demo-scripts/omp_parsec.c) – пример использования конструкции section. Задание: перед запуском, попытайтесь угадать вывод программы, потом проверьте.
* [omp_sumarray.c](demo-scripts/omp_sumarray.c) – пример использования редукции. Обратите внимание на конструкцию #pragma omp parallel for – в чем разница между этой конструкцией и #pragma omp parallel … #pragma omp for


2.) Программы с багами – примеры программ, которые надо починить.
* [omp_bugreduction.c](fix-bugs/omp_bugparfor.c) – код для скалярного произведения двух векторов. Дополнить функцию dotprod, проверить баги в #pragma omp, проверить результат. [20 %]
```
make test_omp_bugparfor 
```
[Output](result/omp_bugparfor.txt)

* [omp_bugreduction.c](fix-bugs/omp_bugreduction.c) – Найти и устранить ошибки. [20 %]
```
make test_omp_bugreduction 
```
[Output](result/omp_bugreduction.txt)

3.) Написать параллельную программу [programme](monte-carlo-pi/main.c), использующую метод Монте-Карло для оценки числа pi. 
Случайным образом (аккуратнее с генератором случайных чисел! Пример в лекции) кидаете точку в единичный квадрат. 
В этот же квадрат вписан круг. Если точка попала в круг, увеличиваете счетчик. Затем находите отношение точек, 
попавших в круг к общему числу точек. Зная площади квадрата и круга, находите приблизительно число pi. [60 %]
```
make test_monte-carlo-pi
```
[Output](result/monte-carlo-pi.txt)