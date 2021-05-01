import math

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    sum = 0
    for x in arr:
        sum += math.pow(x,2)
    print(round(sum%10))