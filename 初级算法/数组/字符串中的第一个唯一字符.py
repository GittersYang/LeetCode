"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {c: s.count(c) for c in set(s)}
        return ([ i for i, c in enumerate(s) if d[c] == 1]+ [-1])[0]
