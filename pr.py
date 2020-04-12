def _not_divisible(n):
    return lambda x: x % n > 0

p = filter(_not_divisible(3), [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(p))