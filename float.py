x=float(input())
y=int(input())
ans=[]
x=str(int(x*(10**y)))
x=[str(x) for x in x]
x.insert(-y, '.')
x=''.join(str(i) for i in x)
print(x)
