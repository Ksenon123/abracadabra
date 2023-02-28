import numpy as np

matrix_2 = np.array([[3., 2., 7.], [4., 1., 8.], [6., 3., 7.]])
matrix_3 = np.array([[4., 3., 2., 7.], [6., 1., 1., -2], [7., 5., 8., 1.], [9., 5., -3., -5.]])

new_array_2 = round(np.linalg.norm(matrix_2), 3)
new_array_3 =round(np.linalg.norm(matrix_3), 3)

print(new_array_2)
print(new_array_3)