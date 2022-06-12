import numpy as np

def inner_dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))

x = np.array([0, 1, 1])
y = np.array([1, 1, 1])

print("The dot product of x and y is: ", inner_dot(x, y))