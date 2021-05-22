N,X=map(int,input().split())
nums=list(map(int,input().split()))#map니라는 객체안에[1,10,4,9,2]
# print(N)
# print(X)
# print(nums)
for x in nums:
        # print(x,end=' ')
        if x<X:
                print(x,end=' ')