# from itertools import combinations
 
# def containsNearbyDuplicate(nums, k):
#     numsDict = {key:[] for key in set(nums)}
    
#     # print("numsDict-0", numsDict)

#     for i, num in enumerate(nums):
#         numsDict[num].append(i)
    
#     # print("numsDict-1", numsDict)


#     for num in set(nums):
#         # numsDict[num] = [list(combinations(numsDict[num], 2)) for num in set(nums) if len(numsDict[num]) >= 2]
#         if len(numsDict[num]) >= 2:
#             numsDict[num] = list(combinations(numsDict[num], 2))
#         else:
#             numsDict[num] = list()

#     # print("numsDict-2", numsDict)
    

#     for key in set(nums):
#         # print('key ', key)
#         for pair in numsDict[key]:
#             # print('pair ', len(pair))
#             if len(pair) == 2 and abs(pair[0] - pair[1]) <= k:
#                 return True

#     return False
# The above code works but its time complexity is high about n2 + n

       
# nums = [1,2,3,1]
# k = 3

# nums = [1,0,1,1]
# k = 1

nums = [1,2,3,1,2,3]
k = 2

print(containsNearbyDuplicate(nums, k))

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}
        for i, num in enumerate(nums):
            if num in store and abs(i-store[num]) <= k:
                return True
            store[num] = i
        return False