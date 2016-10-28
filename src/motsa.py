# coding: utf-8

# author: RaPoSpectre
# time: 2016-09-20

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        num = len(nums1)
        if num % 2 == 1:
            index = (num + 1) / 2 - 1
            return nums1[index]
        else:
            li = num / 2 - 1
            ri = (num + 2) / 2 - 1
            return (nums1[li] + nums1[ri]) / 2.0
