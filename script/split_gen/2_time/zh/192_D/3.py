def solve(x, m):
    d = int(max(x))
    l = len(x)
    if l == 1:
        if d <= m:
            return 1
        else:
            return 0
    else:
        # 二分法
        left = d
        right = m + 1
        while right - left > 1:
            mid = (left + right) // 2
            s = 0
            for i in range(l):
                s += int(x[i]) * (mid ** (l - i - 1))
            if s <= m:
                left = mid
            else:
                right = mid
        return left - d
