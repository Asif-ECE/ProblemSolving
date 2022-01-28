# You are given an integer array nums. A number x is lonely when it appears only once,
# and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

# Return all lonely numbers in nums. You may return the answer in any order.

class Solution(object):
    def findLonely(self, nums):

        lonely = {}

        for i in nums:
            if i in lonely:
                lonely[i] = False
            elif (i+1) in lonely:
                if (i-1) in lonely:
                    lonely[i+1] = False
                    lonely[i] = False
                    lonely[i-1] = False
                else:
                    lonely[i+1] = False
                    lonely[i] = False
            elif (i-1) in lonely:
                if (i+1) in lonely:
                    lonely[i-1] = False
                    lonely[i] = False
                    lonely[i+1] = False
                else:
                    lonely[i-1] = False
                    lonely[i] = False
            else:
                lonely[i] = True
            
        retList = [x for (x,y) in lonely.items() if y==True]
        return retList
