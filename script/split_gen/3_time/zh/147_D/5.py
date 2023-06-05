def get_xor_sum(n, a_list):
    xor_sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            xor_sum += a_list[i] ^ a_list[j]
    return xor_sum
