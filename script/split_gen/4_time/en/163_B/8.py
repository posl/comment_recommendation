def max_hang_out_days(n, m, a):
    if n < sum(a):
        return -1
    else:
        return n - sum(a)
