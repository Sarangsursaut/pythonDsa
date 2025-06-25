class Solution:
  # basic solution 
  def singleNumber(self,num:list[int])->int:
    n=len(num)
    hash_map=dict()
    for i in range(n):
      hash_map[num[i]]=hash_map.get(num[i],0)+1
    for k in hash_map:
      if hash_map[k]==1:
        return k

  #optimal solution  
  def singleNumberSecond(self,num:list[int])->int:
    ans=0
    for i in range(0,len(num)):
      ans=ans^num[i]
    return ans

d=Solution()
list=[5,2,1,1,5,2,3]
print(d.singleNumber(list))
print(d.singleNumberSecond(list))


