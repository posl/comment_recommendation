def max_sum(N, K, V):
    max_sum = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if K >= (j-i):
                sum = 0
                for k in range(i, j):
                    sum += V[k]
                max_sum = max(max_sum, sum)
    return max_sum
