def get_max_sum(n, m, a):
    # 先计算出每个元素的贡献
    # 用一个数组保存，数组的每个元素表示以该元素为结尾的子数组的最大值
    # 递推公式为：f[i] = max(f[i-1] + i*a[i], i*a[i])
    # 由于f[i]只与f[i-1]相关，因此可以用一个变量来保存
    # 递推公式为：f = max(f + i*a[i], i*a[i])
    f = 0
    for i in range(m):
        f += (i+1) * a[i]
    res = f
    for i in range(m, n):
        f = max(f + (i+1) * a[i] - i * a[i-m], (i+1) * a[i])
        res = max(res, f)
    return res
