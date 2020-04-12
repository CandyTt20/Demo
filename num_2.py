# import numpy as np
# l = [1, 2, 3, 4]
# ar = np.array(l)
# print(ar.shape)
# ar1 = ar.reshape(1, -1)
# print(ar1)
# ar2 = ar1.reshape(4,)
# print(ar2)
# ar3 = ar1.flatten()
# print(ar3)
# p1 = np.ones(4).reshape(2, 2)
# print(p1)
# p2 = np.zeros((3, 3), dtype=int)
# print(p2)
# print(p1*2)
# p = np.arange(1, 9)
# print(p[0:1])
# x = [1, 2, 3, 4, 5, 6][1:3]
# print(x)
import numpy as np
# arr1 = np.arange(0, 8).reshape(2, 4)
# arr2 = np.arange(8, 16).reshape(2, 4)

# arr3 = np.hstack((arr1, arr2))
# # print(arr3)
# arr4 = np.concatenate((arr1, arr2), axis=1)
# # print(arr4)
# print( np.vsplit(arr1,2))
a1 = np.arange(1, 9).reshape(2, 4)
a2 = 2 * a1
# print(a1)
# print(a2)
# print(a1 * a2)
a3 = a1
print(id(a1))
print(id(a3))
