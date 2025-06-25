def covert_binary_to_number(a):
  power=0
  result=0
  for i in reversed(a):
    result +=i*2**power
    power+=1
  print(result)
list=[1,1,0,1]
covert_binary_to_number(list)