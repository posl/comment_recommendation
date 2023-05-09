def round_of_n(num, n):
    num = str(num)
    if len(num) > n:
        return int(num[:-n] + '0' * n)
    else:
        return 0
