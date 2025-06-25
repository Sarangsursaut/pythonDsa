def Check__number_powerOfTwo(a):
  result=a&a-1
  if result ==0:
    print('n is a power of two')
  else:
    print("number is not a power of two")
Check__number_powerOfTwo(128)