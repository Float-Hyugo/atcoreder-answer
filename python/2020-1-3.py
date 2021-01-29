n,m = map(int,input().split())
a = map(int,list(input()))
b = map(int,list(input()))

c = set(a) & set(b)
c.sort()
s = '\N'.join(c)
print(s)
