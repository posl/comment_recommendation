def solve(N):
    # write code here
    if N == 0:
        return 0
    if N == 1:
        return 2
    # 二分法
    l, r = 0, N
    while l < r:
        mid = l + (r - l) // 2
        if mid ** 3 + mid ** 2 * 3 + mid * 3 + 1 >= N:
            r = mid
        else:
            l = mid + 1
    return l
