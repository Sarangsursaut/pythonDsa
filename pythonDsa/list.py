#geeksforgeeks list basic question
#User function Template for python3
class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        n=len(arr)
        for i in range(0,n):
            if arr[i]==x:
                return i
        
d=Solution()
d.search([1,2,3,4],3)
