def miniBitCount_firstMethod(start:int,goal:int)->int:
  ans=start^goal
  count=0
  for i in range(0,32):
    if ans & (1<<i) !=0:
      count +=1
  print(count)
miniBitCount_firstMethod(13,8)#timecomplexcity=0(32) and spaceComplexcity=0(1)


def miniBitCount_secoundMethod(start,goal):
  ans = start^goal
  count=0
  while ans>0:
    if ans%2!=0:
      count+=1
    ans=ans//2
  print(count)
miniBitCount_secoundMethod(13,5)#timeComplexcity=0(log2n) and spaceComplexcity=0(1)

