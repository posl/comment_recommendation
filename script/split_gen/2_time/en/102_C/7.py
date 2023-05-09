def get_min_sadness(N, A):
    A = sorted(A)
    if N % 2 == 0:
        return sum([abs(A[i] - (N // 2 - i)) for i in range(N)])
    else:
        return sum([abs(A[i] - (N // 2 - i)) for i in range(N)]) + abs(A[N // 2] - N // 2)
