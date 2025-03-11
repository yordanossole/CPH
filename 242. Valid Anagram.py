class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if "".join(sorted(s)) == "".join(sorted(t)):
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False
        
        counter = dict()

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        return True