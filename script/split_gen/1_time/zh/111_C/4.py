def min_replace_count(n, v):
    # 通过排序找出最小值和最大值
    v = sorted(v)
    # 最小值和最大值相等，说明所有元素都相等，无法构造/\/\/\/
    if v[0] == v[-1]:
        return n // 2
    # 最小值和最大值不相等，说明可以构造/\/\/\/
    else:
        # 构造/\/\/\/需要替换的元素个数
        return n // 2 - v.count(v[0])
