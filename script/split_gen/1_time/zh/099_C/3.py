def get_min_num(n):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        min_num = 100000
        for i in [1, 6, 9]:
            num = get_min_num(n - i)
            if num != -1 and num < min_num:
                min_num = num
        return min_num + 1
