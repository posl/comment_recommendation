def get_max_xor_sum(N, A):
    if N == 1:
        return A[0]
    if N == 2:
        return A[0] ^ A[1]
    else:
        A.sort()
        return A[-1] ^ A[-2] + get_max_xor_sum(N-2, A[:-2])
