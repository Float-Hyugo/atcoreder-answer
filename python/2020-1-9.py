N,M map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
c = 0
for x in A:
  for i,v = enumerate(B):
    if x < v:
      c += M - i
      break
print(c)
