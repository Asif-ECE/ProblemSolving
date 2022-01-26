"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

"""

class Solution(object):
    #initial solution
    def validMountainArray(self, arr):
        if len(arr)>=3 and arr[0]<arr[1]:
            # [3,6,5]
            left = True
            right = False
            for i in range(1,len(arr)):
                if arr[i-1]<arr[i] and left:
                    if i == len(arr)-1:
                        return False
                    right = True
                elif arr[i-1]>arr[i] and right:
                    left = False
                elif arr[i-1]==arr[i]:
                    return False
                elif left == False and right == True and arr[i-1]<arr[i]:
                    return False
            return True
        else:
            return False

    #alternative solution
    def vMA(self, arr):
        if len(arr)>=3 and arr[0]<arr[1]:
            i = 0
            n = len(arr)
            while(i<n and arr[i]<arr[i+1]):
                i += 1
            if i==n-1 or i==0 or arr[i]==arr[i+1]:
                return False
            while(i<n and arr[i]>arr[i+1]):
                i += 1
            return i==n-1
        else:
            return False
