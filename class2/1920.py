# n=int(input())
# N=list(map(int,input().split()))
# m=int(input())
# M=list(map(int,input().split()))
# for i in range(len(M)):
#     if M[i] in N:
#         print(1)
#     else:print(0)
#시간 초과

N=int(input())
A=list(map(int,input().split()))
A.sort()
M=int(input())
B=list(map(int,input().split()))
for target in B:
    #x가 A안에 들있으면 1 출력
    #그렇지 않으면 0 출력
    left=0
    right=len(A)-1
    flag=False
    while left<= right:#이분 탐색의 조건은 항상 이거
        mid=(left+right)//2
        if target <A[mid]:right=mid-1
        elif target >A[mid]:left=mid+1
        elif target==A[mid]:
            flag=True
            break
    if flag:print(1)
    else:print(0)
