def check_ith_index_setOrNot_leftShift(a,index):
  p=1<<index
  if a&p==0:
    print('not set')
  else:
    print('set')
check_ith_index_setOrNot_leftShift(1,2)

def check_ith_index_setOrNot_rightShift(a,index):
  p=a>>index
  if 1&p==0:
    print('not set')
  else:
    print('set')
check_ith_index_setOrNot_rightShift(13,2)
