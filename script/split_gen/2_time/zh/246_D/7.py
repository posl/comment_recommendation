def solve(n):
    # 二分
    l = 0
    r = 10 ** 18
    while r - l > 1:
        mid = (l + r) // 2
        if mid ** 3 >= n:
            r = mid
        else:
            l = mid
    return r
print(solve(int(input())))
