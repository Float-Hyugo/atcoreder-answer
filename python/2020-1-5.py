N = int(input())
S = list(input())
l = [i for i in S if i in ['I','O']]
if l[0] == 'I' and l[-1] == 'I' and l in ['O']:
  print("Yes")
else:
  print("No")
