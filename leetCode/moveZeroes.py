# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-1
        x = 0

        while x<=l:
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
                l -= 1
            else:
                x += 1
                