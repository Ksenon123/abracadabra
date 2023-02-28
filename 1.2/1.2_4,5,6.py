import numpy as np

a = np.array([[4,2],[9,1]])
b = np.array([[5,3],[2,5]])

c = np.concatenate((a, b), axis=1)
print('Задание 1_4 ',c)
result = c[0:2, 0:1]

print("Задание 1_5 ", result)

max_value = np.max(result)
min_value = np.min(result)
sum_value = np.sum(result)

print("Задание 1_6")
print(f'Максимальное значение массива: {max_value}')
print(f'Минимальное значение массива: {min_value}')
print(f'Сумма всех элементов массива: {sum_value}')
