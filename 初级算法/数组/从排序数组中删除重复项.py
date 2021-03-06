"""给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

方法一 cpp
----------------------------------------------------------
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0;
        int j=1;
        if(nums.size()<=1) return nums.size();
        for(;j<nums.size();j++){
            if(nums[i]!=nums[j]){
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
        }
    
};
方法二
----------------------------------------------------
"""
i=0
while i<len(nums)-1:
    if nums[i]==nums[i+1]:
        nums.remove(nums[i])
    else:
        i=i+1
return len(nums)
"""
方法三 优秀
-------------------------------------------------------
“”“
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        l = len(nums)
        if l < 2:
            return l
        nums.sort()
        start = 0
        for x in range(1,l):
            if nums[start] != nums[x]:# 这块是不等于
                nums[start+1] = nums[x]
                start += 1
        return start+1
