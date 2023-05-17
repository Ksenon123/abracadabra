import numpy as np
import random

a = np.array([random.randint (0, 100) for i in range(0, 100, 1)])

print(a)

count = 0

for item in a:
    if item>50:
        count += 1

print("количество элементов списка, удовлетворяющих заданному условию:", count)