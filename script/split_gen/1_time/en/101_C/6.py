def min_operations(N, K, A):
    count = 0
    for i in range(0, N-K):
        if A[i] < A[i+K]:
            count += 1
    return count + 1
