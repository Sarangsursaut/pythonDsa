def check(a):
  k=[]
  while a>0:
    if a%2==0:
      k.append(0)
    else:
      k.append(1)
    a=a//2
  k.reverse()
  print(k)
check(13)