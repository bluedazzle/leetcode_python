# coding: utf-8

# author: RaPoSpectre
# time: 2016-09-20

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, itm in enumerate(nums):
            other = target - itm
            try:
                posi = nums.index(other)
                if posi != i:
                    return sorted([posi, i])
            except ValueError:
                pass
