t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    if sum(nums[0:2]) ==  nums[2]:
        print('YES')
    elif sum(nums[1:]) == nums[0]:
        print('YES')
    elif nums[0]+nums[2] == nums[1]:
        print('YES')
    else:
        print('NO')