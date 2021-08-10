N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    left = 0
    right = N - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            flag = True
            break
        elif target < nums[mid]: right = mid - 1
        elif target > nums[mid]: left = mid + 1
    if flag: print(1)
    else: print(0)