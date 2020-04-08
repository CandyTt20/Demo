# def f(n):
#     s = 1
#     k = 1
#     while k <= n:
#         s = k *s
#         k = k + 1
#     return s
# def g(n):
#     if n == 0:
#         return 1 
#     else:
#         return g(n-1)*n

# print(g(5))

L = []
# L.append(1)
for i in range(0,50):
    L.append(2*i+1)
# print(L)
L1 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L1[1:3])
# print('Michael'[1:len('Michael')-1])
# print(' Michael ')
# s = input('enter:')
# def count_(s):
#     while i <=len(s):
#         if 
def null_string(n):
    string = ''
    for i in range(0,n):
        string = string + ' '
    return string    
# print(len(null_string(0)))
def cut_front(st):
    count = 0
    for i in range(0,len(st)):
        if st[0:i] == null_string(i):
            count = i
    return count
# print(cut_front('   sa'))
def cut_tail(st):
    count = 0
    for i in range(0,len(st)):
        if st[-i:] == null_string(i):
            count = i
    return count
# print(cut_front('sa'))

def trim(st):
    return st[cut_front(st):len(st)-cut_tail(st)]

# print(cut_front('  sf '))
# print(cut_tail('  sf '))
# print('  sf '[cut_front('  sf '):len('  sf ')-cut_tail('  sf ')])
print(trim('  sfas '))
# print('1234'[2:4])