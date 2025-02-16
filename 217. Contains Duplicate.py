class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = dict()
        # count = {num:0 for num in set(nums)}
        
        for num in nums:
            if not num in count.keys():
                count[num] = 1
            else:
                count[num] += 1
        return any([x for x in count.values() if x > 1])