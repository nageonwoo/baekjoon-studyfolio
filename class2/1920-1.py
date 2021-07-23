# 함수버전

def isIn(A, target):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < A[mid]: right = mid - 1
        elif target > A[mid]: left = mid + 1
        elif target == A[mid]: return True
    return False

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
for target in B:
    if isIn(A, target): print(1)
    else: print(0)