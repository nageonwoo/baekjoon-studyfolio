max = 1
maxIdx = 0
for i in range(1, 10):
    a = int(input())
    if a > max:
        max = a
        maxIdx = i
print(max)
print(maxIdx)