"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""
# 方法1 by 杨
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-k
        a = nums[:i]
        b = nums[i:]
        nums[:] = b+a#不能是nums[]
        # 缩略成 
        #n=len(nums)
        #nums[:]=nums[n-k:]+nums[:n-k]
