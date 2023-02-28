import numpy as np

a = np.array([[2.3,5.1,4.7],[3.5,6.6,1.5],[8.4,3.1,9.2]])
b = np.array([[4.3,8.1,6.1],[3.7,6.2,1.5],[2.4,5.7,4.7]])

a_rows = a.shape[0] # количество строк массива а
a_columns = a.shape[1] # количество столбцов массива а

b_rows = b.shape[0] # количество столбцов массива b
b_columns = b.shape[1] # количество столбцов массива b

print("Количество строк массва a", a_rows)
print("Количество столбцов массва a", a_columns)
print("Количество строк массва b", b_rows)
print("Количество столбцов массва b", b_columns)