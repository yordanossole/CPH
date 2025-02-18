class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        temp = []
        result = []
        l = len(nums)
        for i in range(l):
            if i+1 != l and nums[i+1] == nums[i]+1:
                temp.append(nums[i])
            else:
                temp.append(nums[i])
                x = str(temp[0])
                y = str(temp[-1])
                if x!=y: 
                    z = x + '->' + y
                    result.append(z)
                else: 
                    result.append(x)
                temp = []
        return result

# optimised
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        result = []
        for i in range(len(nums)):
            if i+1 == len(nums) or nums[i+1] != nums[i]+1:
                if start == nums[i]:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i]}")
                if i+1 != len(nums):
                    start = nums[i+1]
        return result