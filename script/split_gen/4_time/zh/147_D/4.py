def xor_sum(a):
    n = len(a)
    if n == 1:
        return 0
    else:
        return (a[0] ^ a[1]) + xor_sum(a[1:])
