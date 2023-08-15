s=input()
b=[]
k=["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(s)):
  if s[i] not in k: 
    b.append(s[i])
for i in range(len(b)):
  print(b[i],end='')
