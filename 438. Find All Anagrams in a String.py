class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if len(s) < len(p):
            return []
        left = 0
        result = []
        anagram = {}
        window = {}

        for c in p:
            anagram[c] = anagram.get(c, 0) + 1
        
        for i in range(k):
            window[s[i]] = window.get(s[i], 0) + 1      
        if anagram == window:
                result.append(left)
        for right in range(k, len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            if anagram == window:
                result.append(left)
        return result