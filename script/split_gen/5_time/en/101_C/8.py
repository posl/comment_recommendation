def min_operations(N, K, A):
    count = 0
    for i in range(0, N, K-1):
        count += 1
    return count
