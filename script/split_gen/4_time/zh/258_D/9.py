def solve(N, X, A, B):
    # 二分法
    # 二分法的初始值
    left = 0
    right = 10 ** 18
    # 二分法的循环
    while right - left > 1:
        mid = (left + right) // 2
        # 检查mid是否满足条件
        if check(mid, N, X, A, B):
            right = mid
        else:
            left = mid
    return right
