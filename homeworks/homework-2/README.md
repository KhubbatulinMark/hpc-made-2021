# Homework #2

1.) Реализовать классическое перемножение матриц и умножение матрицы на вектор на C/C++. (25%)
- Реализация лежит в папке [matmul](./matmul)

2.) Разбейте на модули, со статической линковкой скомпилируйте текст, подготовьте Makefile, проверьте флаги -g, -O3 (25%)
- Реализация лежит в папке [matmul](./matmul)

3.) Измерьте времена исполнения для размеров $N = 500, 512, 1000, 1024, 2000, 2048 (25%)
В т.ч. проведите сравнение с виртуальной машиной, докером (опционально)
- Тесты в основной OC [tests](./matmul/tests/tests.txt)
- Тесты в Докере [docker-tests](./matmul/tests/docker-tests.txt)

`По результатам тестов видно, что скорость работы в докере значительно ниже, чем на основной ОС (Даже слишком сильно, возможно это из-за проблем с виртуализацией на М1) `

4.) И базовые скрипты баш (25%)
- Organize FOR loop printing the even numbers only from 100 to 1000  [script](scripts/even_numbers.sh)
- Initialize the array of 10-20 elements and organize FOR loop printing the elements of array [script](scripts/print_elem_array.sh)
- Compute 100 + 0.5 in bash [script](scripts/compute_100_0_5.sh)
- Check if file ”Linux” exists in present directory. 
  If yes, print message ”course”. 
  If no, print message ”very easy” and create the ”Linux” file with text ”course is easy” [script](scripts/check_subdir.sh)
  
5.) Бонус за линпак (+20%)
- Был использон этот [тест](https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html)
- CPU Apple M1 
- Запуск `cd linpacl && zsh runme64`
- [Результаты](./linpack/lin_cd64.txt)
6. Супербонус протестируйте алгоритм Штрассена (+20%)