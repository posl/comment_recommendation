def max_xor(n, k, a):
    max_xor = 0
    for i in range(k+1):
        xor = 0
        for j in range(n):
            xor += i ^ a[j]
        if xor > max_xor:
            max_xor = xor
    return max_xor
