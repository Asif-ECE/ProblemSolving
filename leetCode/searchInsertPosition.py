# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where
# it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)-1
        left = 0
        right = n
        
        while left<right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
                if nums[left] > target:
                    return left
                if left == n and nums[left] != target:
                    return n+1
            else:
                right = mid-1
                if nums[right] < target:
                    return right+1
                if right == 0 and nums[right] != target:
                    return 0
                
            if left == right:
                return left
        
        if nums[left] == target:
            return left
        elif nums[left] > target:
            return left
        else:
            return left+1
