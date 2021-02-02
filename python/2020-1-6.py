N = int(input())
A = list(map(int,input().split()))
mx = 0
idx = 0
for l,v in enumerate(A):
  if v > mx:
    mx = v
    idx = l
bfr = sum(A[:l])
after = sum(A[l+1:])
print(bfr)
print(after)
