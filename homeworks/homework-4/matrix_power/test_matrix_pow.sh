#!/usr/bin/env bash

array=(
  2 4 8 16 32 64 128
)

for pow in "${array[@]}"
do
  ./matrix_power/matrix_pow.exe 1024 $pow >> result/matrix_pow.txt
done