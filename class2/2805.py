N, target = map(int, input().split())
heights = list(map(int, input().split()))

l, r = 0, max(heights)
ans = 0
while l <= r:
    m = (l + r) // 2
    take = 0
    for h in heights:
        cut = h - m
        if cut > 0: take+=cut
    if take >= target: l = m + 1 # 높이를 높임
    elif take < target: r = m - 1 # 높이를 낮춤
print(r)