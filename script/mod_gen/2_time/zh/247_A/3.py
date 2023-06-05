def judge(x):
    # 二分法查找
    l = 0
    r = x
    while r - l > 1:
        m = (l + r) // 2
        if m ** 3 + m ** 2 * m + m * m ** 2 + m ** 3 < x:
            l = m
        else:
            r = m
    return r ** 3 + r ** 2 * r + r * r ** 2 + r ** 3 == x

if __name__ == '__main__':
    judge()