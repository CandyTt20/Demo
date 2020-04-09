L = [x*x for x in range(0,10)]
# print(L)

g = (x*x for x in range(0,10))
# print(next(g))
# print(next(g))
# for n in g:
#     print(n)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def gen_fib(n):
    
    s = 1
    while s <= n:
        yield fib(s)
        s = s+1

# for i in gen_fib(5):
#     print(i)
next(gen_fib(5))
# print(type(gen_fib(5)))


def f(n):
    a1 = 1
    a2 = 1
    s = 0
    while s<n:
        yield a1
        a1,a2 = a2,a1+a2
        s = s+1

# print(next(f(5)))
j = f(6)
while True:
    try:
        x = next(j)
        print('j:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break