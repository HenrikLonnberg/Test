import math
import cmath
import numpy as np

# p = math.sin(math.pi / 2 + math.pi)
#
# print(p)
#
# t = complex(1, 1)
# print(t)
#
# t1 = cmath.phase(t)
# print(t1)
#
# vector = cmath.polar(t)
# print(vector)

a = np.array([[1, 2, 3],[4, 5, 6]])

b = np.array([[7, 8, 9],[10, 11, 30]])
b = b.T # transposing

print(b)
print(b.dot(a))
