def func(N, A):
    if N == 2:
        return min(A)
    min_A = min(A)
    max_A = max(A)
    if min_A == max_A:
        return min_A
    min_A_idx = A.index(min_A)
    max_A_idx = A.index(max_A)
    if min_A_idx > max_A_idx:
        min_A_idx, max_A_idx = max_A_idx, min_A_idx
    A[min_A_idx] = min_A
    A[max_A_idx] -= min_A
    return func(N, A)
