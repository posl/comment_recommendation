def find_max_k(n):
    k = 0
    while 2 ** k <= n:
        k += 1
    return k - 1
