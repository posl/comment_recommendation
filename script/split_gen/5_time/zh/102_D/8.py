def get_max_min_diff(a):
    # 1.先将a排序
    a.sort()
    # 2.找出最大值和最小值
    max = a[-1] + a[-2] + a[-3]
    min = a[0] + a[1] + a[2]
    return max - min
