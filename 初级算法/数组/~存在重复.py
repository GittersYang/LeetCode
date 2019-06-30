"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
"""
#method1  python中的集合没有重复元素 yang-------------------------
# return len(nums) != len(set(nums))
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(list(set(nums)))
        if a < len(nums):
            return True
        else:
            return False
# 2,1 ,2.2 均有问题------------------------
# method 2.1  yang  使用排序 循环-------------------------
class Solution:#  此方法空集时报错
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return True
                break
            else:
                return False
# method 2.1  yang  使用排序 循环-------------------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)>1:
            nums.sort()
            for i in range(len(nums)):
                if nums[i]==nums[i+1]:
                    return True
                    break
                else:
                    return False
        else:
            return False
                
