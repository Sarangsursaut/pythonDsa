#User function Template for python3
#union of twolist
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        n=len(a)
        m=len(b)
        set=[]
        for i in range(0,n):
            set.append(a[i])
        for j in range(0,m):
            if b[j] not in set:
                set.append(b[j])
        return(set)
b=Solution()
b.findUnion([1, 2, 3, 4, 5],[1, 2, 3, 6, 7])
