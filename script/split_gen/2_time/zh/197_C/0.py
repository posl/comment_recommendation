def get_min_xor(a):
    min_xor = 2**30
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            min_xor = min(min_xor, a[i]^a[j])
    return min_xor
