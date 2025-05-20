n = int(input())

waiting_time = [0] # prefix sum
cur_sum = 0
counter = 0

nums = list(map(int, input().split()))
nums.sort()

for i in range(n-1):
    cur_sum += nums[i]
    waiting_time.append(cur_sum)

dic = dict(zip(nums, waiting_time))
for key in dic:
    if key >= dic[key]:
        counter += 1
print(counter)
