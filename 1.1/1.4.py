import numpy # импортируем библиотеку 

#5x+4y=14
#2x-6y=-2

M1 = numpy.array([[5., 4.], [2., -6.]]) # Матрица (левая часть системы)
v1 = numpy.array([14., -2.]) # Вектор (правая часть системы)
#Запишем все числа с точкой, т.к. иначе они будут участвовать в целочисленных операциях (остатки от деления будут отбрасываться)
new_array = numpy.linalg.solve(M1, v1) 
print(new_array)