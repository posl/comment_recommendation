def get_min_xor(n, a):
    min_xor = 2**30
    for i in range(n):
        for j in range(i+1, n+1):
            xor = a[i]
            for k in range(i+1, j):
                xor = xor ^ a[k]
            if xor < min_xor:
                min_xor = xor
    return min_xor
