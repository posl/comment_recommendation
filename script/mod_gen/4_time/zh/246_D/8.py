def f(n):
    # 二分法
    l = 0
    r = 10 ** 18
    while r - l > 1:
        m = (l + r) // 2
        if m ** 3 < n:
            l = m
        else:
            r = m
    return r
n = int(input())
print(f(n))
