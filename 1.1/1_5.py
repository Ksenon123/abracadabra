import numpy as np

a = np.array([[2.3, 5.1, 4.7], [3.5, 6.6, 1.5], [8.4, 3.1, 9.2]])
b = np.array([[4.3, 8.1,6.1],[3.7,6.2,1.5],[2.4,5.7,4.7]])

cos_a = np.cos(a)
sin_b = np.sin(b)
sum_a_b = sin_b + cos_a
print("Косинус каждого элемента массива a: ", cos_a)
print("Косинус каждого элемента массива b: ",sin_b)
print("Сумма массивов a + b = ", sum_a_b)