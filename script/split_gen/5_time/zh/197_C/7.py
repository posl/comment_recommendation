def get_min_xor(a):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2:
        return a[0]^a[1]
    else:
        min_xor = 2**30
        for i in range(1,n):
            xor = get_min_xor(a[:i])^get_min_xor(a[i:])
            if xor < min_xor:
                min_xor = xor
        return min_xor
