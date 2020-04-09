def triangle(n):
    s = list(range(0,n))
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    else:
        for i in range(0,n):
            if i == 0 or i == n-1:
                s[i] = 1
            else:
                s[i] = triangle(n-1)[i] + triangle(n-1)[i-1]
        return s
# print(triangle(4))

for i in range(1,10):
    print(triangle(i))