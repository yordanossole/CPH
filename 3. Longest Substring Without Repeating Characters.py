class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        sub_str = set()

        for right in range(len(s)):
            while s[right] in sub_str:
                sub_str.remove(s[left])
                left += 1
            sub_str.add(s[right])
            max_len = max(max_len, len(sub_str))
        
        return max_len
            