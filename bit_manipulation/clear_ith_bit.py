def set_ith_bit(a,index):
  p=1<<index
  p=~p
  result=a&p
  print(result)
set_ith_bit(9,3)