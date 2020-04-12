a = [12, 33, 5, 2, 52, 3]
# print(sorted(a,key=abs))


def lazy_sum(*args):
    def sum():
        s = 0
        for i in args:
            s = s + i
        return s
    return sum


f = lazy_sum(1, 2, 3)
# print(f)
# print(f())
print(f.__name__)