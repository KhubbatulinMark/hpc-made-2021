#!/usr/bin/env bash

array=(
  apple banana "Fruit Basket" orange Avocado
  123 32.123123 {}[] ...213 "Hello" "and some other element"
)

for element in "${array[@]}"
do
  echo $element
done