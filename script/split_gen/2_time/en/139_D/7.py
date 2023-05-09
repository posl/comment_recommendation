def max_sum(N):
    if N <= 2:
        return N - 1
    else:
        return N + max_sum(N - 1)
