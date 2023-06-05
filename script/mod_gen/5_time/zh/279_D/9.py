def solve(A: int, B: int):
    # 二分法
    # 1. 先计算不操作的情况下的时间
    # 2. 二分法，计算操作的情况下的时间
    # 3. 直到精度满足要求
    def calc(t):
        return t + A / (t ** 0.5)
    left = 0
    right = 10 ** 18
    while right - left > 10 ** -6:
        mid = (left + right) / 2
        if calc(mid) < calc(mid + 10 ** -6):
            right = mid
        else:
            left = mid
    return calc(right)

if __name__ == '__main__':
    solve()