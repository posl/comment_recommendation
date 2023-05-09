def get_max_xor(n, k, a):
    max_xor = 0
    for i in range(n):
        max_xor = max(max_xor, k ^ a[i])
    return max_xor
