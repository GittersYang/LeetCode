"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""

# method1   yang    暴力循环法   为防止多于元素出现 只要appen后 其元素在第二个列表删除  nums2.append(..)-----------------
a = []
for i in nums1:
  if i in nums2:
    a.append(i)
    nums2.remove(i)
 return a 
 
 #  method 2    li    利用双指针  --------------------------
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        a = []
        i = 0
        j = 0
        while(i<len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                a.append(nums1[i])
                i+=1
                j+=1
                
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return a
    # method3     dict    collections.Counter(..)------从列表转化为字典-------------------
class Solution:
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
