import numpy as np
import matplotlib.pyplot as plt
# x1 = np.arange(0, 4)
# print(id(x1))
# x1 = np.arange(0, 4)
# print(id(x1))
# x2 = np.copy(x1)
# # print(id(x1))
# # print(id(x2))
l = []
for i in range(0, 1000):
    l.append(np.random.rand())
# print(l)
plt.hist(l, color='r')
plt.show()
