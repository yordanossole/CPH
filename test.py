def minMovesToSeat(seats, students):
    seats = sorted(seats)
    students = sorted(students)
    
    result = [abs(x-y) for x,y in zip(seats, students)]
    return sum(result)
    
seats = [3,1,5]
students = [2,7,4] #4
seats = [17,10,20,2]
students = [10,9,7,16] #17
seats = [14,3,1,1,17,12,3,19,8]
students = [1,11,12,17,6,1,1,7,10] #18

# print(minMovesToSeat(seats, students))
def maxArea(height):
    n = len(height)
    left = 0 
    right = n-1
    print(left, right)

    while left < right:
        print('entered into the loop')
        if height[left] < height[left + 1]:
            left += 1
            print(left, right)

        elif height[right] < height[right - 1]:
            right -= 1
            print(left, right)
        else:
            break
    if left == right:
        left -= 1
        right += 1

    print('final line')

    return min(height[left], height[right]) * (right - left)

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height = [1,2,1]

print(maxArea(height))