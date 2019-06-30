"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""

# method 1   yang     排序 删除  很耗时  待改进-------------------------
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while(len(nums)>1):
            if nums[0]==nums[1]:
                del nums[0]# del是根据索引删除 remove是删除值  nums.reomve(..)
                del nums[0]# 不是del nums[1]

            else:
                return nums[0]
        else:
            return nums[0]

#  method 2------------------------------------------------------------------
class Solution(object):
    #  是计算和 而不是在列表上减  通过这些不重复的元素和的两倍减去原来nums的和，得到的结果就是单个元素
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        return 2*sum(set_nums)-sum(nums)
#  method3  异或  是转成二进制异或-------------0与这个集合做异或 相当于集合本身相等的两个先异或约掉-------------------------------
class Solution(object):
    # 可用异或运算快速找到只出现依次的数字
    # 两个相同的数字做异或运算结果为0；0与非0数字做异或运算结果为非零运算
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singel_num = 0
        for num in nums:
            singel_num ^= num
        return singel_num
#method 4.1  set集合  效率不高-----------------------------------
class Solution(object):
    # 可用count(num)查找列表nums中单个元素num在列表nums中的个数情况
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        for num in set_nums:
            if nums.count(num) == 1:
                return num


#method 4.1  dict----------------------------------------------------------
class Solution(object):
    # 可用count(num)查找列表nums中单个元素num在列表nums中的个数情况
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for key, val in nums_dict.items():
            if val == 1:
                return key


            
