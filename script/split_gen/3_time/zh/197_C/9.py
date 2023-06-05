def get_min_xor(a):
    a.sort()
    min_xor = 2**30
    for i in range(len(a)-1):
        xor = a[i] ^ a[i+1]
        if xor < min_xor:
            min_xor = xor
    return min_xor
