def find_max_num(n, m, a):
    # 1. 选出最小的数字
    # 2. 从大到小排列
    # 3. 从最大的数字开始，选出最大的数字
    # 4. 重复3，直到火柴棒用完
    # 5. 如果火柴棒用完，但是数字没有选完，那么从头开始选
    # 1. 选出最小的数字
    min_num = 9
    for i in range(m):
        if a[i] < min_num:
            min_num = a[i]
    print('min_num:', min_num)
    # 2. 从大到小排列
    a.sort(reverse=True)
    print('a:', a)
    # 3. 从最大的数字开始，选出最大的数字
    num = ''
    while n > 0:
        for i in range(m):
            if a[i] <= n:
                num = num + str(a[i])
                n = n - a[i]
                break
    print('num:', num)
    # 5. 如果火柴棒用完，但是数字没有选完，那么从头开始选
    if n == 0:
        return num
    else:
        return find_max_num(n, m, a)

if __name__ == '__main__':
    find_max_num()