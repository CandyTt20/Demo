# l = list(range(0, 10))
# # print(l)
# l1 =list(map(str, l))
# # print(l1)

# l2 = (1, 2, 3)
# print(list(map(str,l2)))
# print('sb'+'s')
# print(str.upper('sBsd'))
# print('sBsd'[0:len('sBsd')])
# 'sBsd'[0,len()]


def normal(string):
    header = str.upper(string[0])
    body = str.lower(string[1: len(string)])
    return header + body

# print(normal('sSFvG'))


def normal_list(l):
    return list(map(normal, l))


L = ['adam', 'LISA', 'barT']

print(normal_list(L))
