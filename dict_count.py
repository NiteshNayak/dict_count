# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.

# Input: [2,1,2,5,3,2]
# Output: 2


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        num = len(A) / 2
        mydict = {}
        
        for i in A:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] = mydict[i] + 1
                
        for x,y in mydict.items():
            if y == num:
                return x
