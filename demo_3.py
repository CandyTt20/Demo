# print(isinstance(None,str))
L = ['Hello', 'World', 'Apple']
L1 = ['Hello', 'World', 18, 'Apple','sada','ee',2131, None]
L2 = [x.lower() for x in L1 if isinstance(x,str) ]
print(L2)