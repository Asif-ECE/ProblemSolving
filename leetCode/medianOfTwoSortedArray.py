# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        allInserted = False
        
        if nums1 != [] and nums2 != []:
            for i in range(len(nums2)):
                for j in range(len(nums1)):
                    if nums2[i] <= nums1[j]:
                        nums1.insert(j,nums2[i])
                        break
                    elif j == len(nums1)-1:
                        nums1 = nums1 + nums2[i:]
                        allInserted = True
                        break
                if allInserted:
                    break
        else:
            nums1 = nums1 + nums2

        if len(nums1)%2 == 0 and len(nums1)//2>0:
            x = len(nums1)//2
            return (float(nums1[x-1])+float(nums1[x]))/2
        else:
            x = len(nums1)//2
            return float(nums1[x])
