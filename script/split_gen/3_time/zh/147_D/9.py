def get_xor_sum(a):
    xor_sum = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            xor_sum += a[i] ^ a[j]
    return xor_sum
