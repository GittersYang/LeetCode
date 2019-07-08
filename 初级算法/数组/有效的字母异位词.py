"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        if len(s_dict) != len(t_dict):
            return False
        else:
            for i in s_dict:
                if s_dict[i] != t_dict.get(i):
                    return False

        return True
