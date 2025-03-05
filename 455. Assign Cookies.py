def findContentChildren(g,s):
    # count = 0
    # for i,j in zip(range(len(g)), range(len(s))): 
    #     if s[j] >= g[i]:
    #         count += 1
    # return count



    # --------------
    # count = 0
    # for i in g:
    #     if any(j >= i for j in s):
    #         count += 1
    # return count

    # --------------
    for i in g:
    # if any(j >= i for j in s):
    #     count += 1
        for j in s:
            if j >= i:
                count += 1
                break



g = [1,2,3]
s = [1,1]

# g = [1,2]
# s = [1,2,3]

# g = [10,9,8,7]
# s = [5,6,7,8]
# print(findContentChildren(g,s))

print('1'*3)