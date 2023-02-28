import numpy as np

a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2])

size = a.shape
print("Кол-во строк и стобцов массива:", size)

new_array_1 = np.reshape(a, (9, 1))
print("Массив 1:", new_array_1)

new_array_2 = np.reshape(a, (3, 3))
print("Массив 2:", new_array_2)

max_element_column = np.max(new_array_2, 0)
max_element_row = np.max(new_array_2, 1)

min_element_column = np.min(new_array_2, 0)
min_element_row = np.min(new_array_2, 1)

summa_element_column = np.sum(new_array_2, 0)
summa_element_row = np.sum(new_array_2, 1)

print("Макс кол-во в строке:", max_element_column) #макс кол-во в строке
print("Макс кол-во в столбце:", max_element_row) #макс кол-во в столбце

print("Мин кол-во в строке:", min_element_column) #мин кол-во в строке
print("Мин кол-во в столбце:", min_element_row) #мин кол-во в столбце

print("Сумма кол-во в строке:", summa_element_column)
print("Сумма кол-во в строке:", summa_element_row)