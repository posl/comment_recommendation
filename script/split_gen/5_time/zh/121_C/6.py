def solve(n, m, a, b):
    # 二分查找
    # 二分查找的上下界
    lower = 0
    upper = 10 ** 18 + 1
    # 二分查找的循环
    while lower + 1 < upper:
        # 中间值
        mid = (lower + upper) // 2
        # 可以买到的数量
        num = 0
        # 用mid日元可以买到的数量
        for i in range(n):
            num += min(a[i], mid // b[i])
        # 判断可以买到的数量是否大于等于m
        if num >= m:
            upper = mid
        else:
            lower = mid
    return upper
