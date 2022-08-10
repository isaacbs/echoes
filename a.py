# def firstMissingPositive(nums):
#     l = len(nums)-1
#     miss = 1
#     diff = l
#     for i in nums:
#         if i == miss:
#             print(i, 'help')
#             miss += 1
#         elif i <= l and i >= 0:
#             print(i, 'trap')
#             diff -= 1
#         print('miss', miss, 'diff', diff)
#     if 
            

# l1 = [1,2,3,4,5]
# l2 = [3,4,-1, 1]
# l3 = [4,5,1,2,7]
# print(firstMissingPositive(l2))

def firstMissingPositive(nums):
    tot = 0
    sol = 0
    enum = 1
    for i in nums:
        if i <= len(nums) and i > 0:
            tot += enum
            enum += 1
            sol += i
    return max(1, (sol-tot))

l1 = [1,2,3,4,5]
l2 = [3,4,-1, 1]
l3 = [4,5,1,2,7]
print(firstMissingPositive(l3))