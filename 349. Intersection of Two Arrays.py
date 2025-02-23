class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:       
        st = set(nums1)
        result = []
        for num in nums2:
            if num in st:
                result.append(num)
                st.remove(num)
        return result