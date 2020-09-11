#Даны три целых числа. Выведите значение наименьшего из них

x = int(input())
y = int(input())
z = int(input())

if x <= y or x <= z:
	print(x)
elif y <= x or y <= z:
	print(y)
else:
	print(z)