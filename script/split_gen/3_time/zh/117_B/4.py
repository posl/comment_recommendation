def check_polygon(n, l):
    # 判断是否可以画出多边形
    if n < 3 or n > 10:
        return False
    if len(l) != n:
        return False
    if any([li < 1 or li > 100 for li in l]):
        return False
    # 从大到小排序
    l.sort(reverse=True)
    # 最大边长
    max_len = l[0]
    # 其他边长之和
    other_len = sum(l[1:])
    if max_len < other_len:
        return True
    else:
        return False
