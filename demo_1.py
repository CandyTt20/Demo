classmate = ['s','b','sb']
# print(len(classmate))
# print(classmate[0])
classmate.insert(1,'gg')
# print(classmate)
""" print(classmate.pop(1))
print(classmate) """

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]

# print(L[0][0]) 

""" age = int(input('enter a number:'))
if age > 18:
    print('Your age is', age)
    print('adult')
    pass
else:
    print('Your age is', age)
    print('teen')
    pass """

""" s = 0
for i in range(0,101):
    s = s + i
print(s) 
w = 0
t = 0
while w <= 100:
    t = t + w
    w = w +1
print(t) """
""" 
print(type(range(5)))
print(list(range(5))) """

""" a = 'abc'
print('abc'.replace('a','A'))
print(a.replace('a','A'))
print(a) """

""" def f(x):
    if x>= 0:
        return x
        pass
    else:
        return -x
        pass
print(f(-2)) """

""" def pow(x,n=2):
    s = 0
    f = 1
    while s < n:
        f = f * x
        s = s+1
    return f

print(pow(2)) """

""" def sum(num):
    s = 0
    for i in num:
        s = s + i
    return s
print(sum((1,2,3,4))) """

""" def sum1(*num):
    s = 0
    for i in num:
        s = s + i
    return s
print(sum1(1,2)) """

def key(x,**k):
    print(x,k)

key('a',f = 'f',p = 'r')
print(type({'f': 'f', 'p': 'r'}))

l = {'f': 'f', 'p': 'r'}
print(l["f"])

print()