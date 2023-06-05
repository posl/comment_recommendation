def get_kth_num(k, n, a):
    if k > n * (10**18):
        return k - n * (10**18)
    for i in range(1, 10**18):
        if i not in a:
            k -= 1
            if k == 0:
                return i
