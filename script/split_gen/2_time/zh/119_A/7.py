def max_number(n, m, a):
    # 从大到小排序
    a.sort(reverse=True)
    # 从大到小拼接
    result = ''
    while n > 0:
        for i in range(m):
            if n >= a[i]:
                result += str(a[i])
                n -= a[i]
                break
    return result
