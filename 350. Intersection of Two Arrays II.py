class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                try:
                    nums2.remove(num)
                except:
                    pass
        return result     
            
        