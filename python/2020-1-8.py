N = int(input())
A = list(input())
c = 0
for i,v in enumerate(A):
  if i % 2 == 1:
    if v != 'I':
      c += 1
      continue
  else:
    if v != 'O':
      c += 1
      continue
print(c)
