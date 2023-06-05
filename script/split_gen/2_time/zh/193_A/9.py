def solve(x, m):
    # 二分查找
    if len(x) == 1:
        return 1 if int(x) <= m else 0
    # 二分查找
    min_base = int(max(x)) + 1
    max_base = m + 1
    while min_base < max_base:
        mid_base = (min_base + max_base) // 2
        num = 0
        for i in range(len(x)):
            num = num * mid_base + int(x[i])
            if num > m:
                break
        if num <= m:
            min_base = mid_base + 1
        else:
            max_base = mid_base
    return min_base - int(max(x))
