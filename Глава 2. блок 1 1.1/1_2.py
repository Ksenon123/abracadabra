import numpy as np

a = np.array([[2.3, 5.1, 4.7], [3.5, 6.6, 1.5], [8.4, 3.1, 9.2]])
b = np.array([[4.3, 8.1,6.1],[3.7,6.2,1.5],[2.4,5.7,4.7]])

# сумма
sum_ab = a + b
print(f'Сумма массивов a и b:\n{sum_ab}')

# разность
diff_ab = a - b
print(f'Разность массивов a и b:\n{diff_ab}')

# произведение
prod_ab = a * b
print(f'Произведение массивов a и b:\n{prod_ab}')

# частное
div_ab = a / b
print(f'Частное массивов a и b:\n{div_ab}')