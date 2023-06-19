def get_max_snuke_sum(N, T, X, A):
    max_snuke_sum = 0
    for i in range(N):
        if i == 0:
            max_snuke_sum += A[i]
            continue
        elif T[i] - T[i-1] >= abs(X[i] - X[i-1]):
            max_snuke_sum += A[i]
    return max_snuke_sum
