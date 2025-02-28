class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        max_jump = 0

        for num in nums:
            if max_jump < 0:
                return False
            elif num > max_jump:
                max_jump = num
            max_jump -= 1

        return True