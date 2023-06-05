def find_kth_number(n, k):
    # 二分查找
    # 1. 找到第一个大于等于k的数
    # 2. 如果第一个数就大于等于k，返回k
    # 3. 否则返回k + (k - 1) // (n - 1)
    # 4. 重复上述过程
    l = 1
    r = 1 << 63
    while l < r:
        m = (l + r) >> 1
        if m - m // n >= k:
            r = m
        else:
            l = m + 1
    return r
