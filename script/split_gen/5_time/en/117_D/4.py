def xor_sum(n, k, a):
    max_f = 0
    for i in range(k+1):
        f = 0
        for j in range(n):
            f += i ^ a[j]
        if f > max_f:
            max_f = f
    return max_f
