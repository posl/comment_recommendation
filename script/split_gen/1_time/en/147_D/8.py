def xor_sum(N, A):
    s = 0
    for i in range(N):
        for j in range(i+1, N):
            s += A[i] ^ A[j]
    return s
