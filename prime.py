# f = lambda x,y: x%y==0


# print(f(2,5))


# def fliter_list(n, L):
#     return list(filter(check(n)))

# print(check(3, 6))
# print(lambda n,x: x%n==0)
# def check_lambda():
# return lambda n,x: x%n==0


def kick(L):
    s = []
    for i in range(0, len(L)):
        if L[i] % L[0] != 0:
            s.append(L[i])
    return s


# print(kick([5, 7]))
def try_1(L):
    s = []
    # s.append(L[0])
    while L != []:
        s.append(L[0])
        L = kick(L)
    return s


def prime(n):
    print(try_1(range(2, n+1)))


prime(10000)
