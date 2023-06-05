def get_max_num(a, k):
    num = 0
    for i in range(k-1, -1, -1):
        if a[i] <= num:
            continue
        num = (a[i] - 1) // a[i]
    return num
