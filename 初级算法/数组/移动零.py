"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            try:
                nums.remove(0)
                nums.append(0)
            except:
                return nums

#method 2 --------------
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gen(nums):
            for x in nums:
                if x:
                    yield x
        
        i = 0# 很重要
        for i, n in enumerate(gen(nums)):# enumerate 枚举 
            nums[i] = n
        for i in range(i + 1, len(nums)):
            nums[i] = 0

