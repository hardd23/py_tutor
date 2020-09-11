#Условие
#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!):
#he next number for the number 1534 is 1535.
#The previous number for the number 1534 is 1533.

n = int(input())
m = n + 1
v = n - 1
print("The next number for the number " + str(n) + " is " + str(m) + ".")
print("The previous number for the number " + str(n) + " is " + str(v) + ".")