import numpy as np

matrix_1 = np.array([[2., 8.], [1., -6.]])
matrix_2 = np.array([[3., 2., 7.], [4., 1., 8.], [6., 3., 7.]])
matrix_3 = np.array([[4., 3., 2., 7.], [6., 1., 1., -2], [7., 5., 8., 1.], [9., 5., -3., -5.]])

new_array_1 =np.transpose(matrix_1)
new_array_2 =np.transpose(matrix_2)
new_array_3 =np.transpose(matrix_3)

print(new_array_1)
print(new_array_2)
print(new_array_3)