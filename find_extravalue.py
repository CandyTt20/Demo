def find(L):
    Max = L[0]
    Min = L[0]
    for i in L:
        if i > Max:
            Max = i
        if i < Min:
            Min = i
    return Max,Min

print(find([3,4,532,6,31,6]))
