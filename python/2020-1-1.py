l = map(int,input().split())
r = min(l[1],max(l[2],l[3]))
s = max(r,min(l[2],l[3]))
print(s)
