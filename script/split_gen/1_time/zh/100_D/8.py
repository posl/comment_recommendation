def get_max_abs_sum(a):
    n = len(a)
    s = 0
    for i in range(n):
        s += abs(a[i])
    return s
