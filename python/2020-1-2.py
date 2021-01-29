l = input()
s = list(input())

j = [x for x in s if x == "J"]
o = [x for x in s if x == "O"]
i = [x for x in s if x == "I"]

c = [j,o,i]
x = ""

for a in c:
  for b in a:
    x += b

print(x)
