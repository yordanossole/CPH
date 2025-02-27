class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # arr = list(range(1, len(nums)+1))
        # result = []

        # for num in arr:
        #     if not num in nums:
        #         result.append(num)
        # return result
        arr = set(range(1, len(nums)+1))
        nums = set(nums)
        return list(arr.difference(nums))
                
