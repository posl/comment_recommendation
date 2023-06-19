def solve(n, ab):
    # 二分查找
    # 1. 先求出最大的速度
    max_speed = 0
    for i in range(n):
        max_speed = max(max_speed, ab[i][1])
    # 2. 二分查找
    left = 0
    right = 1000000000
    while right - left > 0.0000000001:
        mid = (left + right) / 2
        time = 0
        for i in range(n):
            time += ab[i][0] / (max_speed - mid * ab[i][1])
        if time > mid:
            left = mid
        else:
            right = mid
    return left
