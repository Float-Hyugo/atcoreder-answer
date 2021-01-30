c = list()
input()
a = map(int,input().split())
b = map(int,input().split())

while True:
  if len(a) == 0 and len(b) == 0:
    breake
  if len(a) == 0:
    c.append(b[0])
    b.pop(0)
    continue
  if len(b) == 0:
    c.append(a[0])
    a.pop(0)
    continue
  if(a[0] <= b[0]):
    c.append(a[0])
    a.pop(0)
    continue
  c.append(b[0])
  b.pop(0)
"\N".join(c)
print(c)
