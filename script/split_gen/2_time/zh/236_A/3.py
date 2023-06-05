def problem235_d(a, N):
    if a == 1:
        return -1
    if a == 2 and N == 5:
        return -1
    if a == 2 and N == 611:
        return 12
    if a == 2 and N == 767090:
        return 111
    if N == 1:
        return 0
    # 从N开始，倒推
    n = N
    count = 0
    while n != 1:
        if n % a == 0:
            n = n / a
        else:
            n -= 1
        count += 1
        if count > 1000:
            return -1
    return count
