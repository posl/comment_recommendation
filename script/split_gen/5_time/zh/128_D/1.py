def max_value(N, K, V):
    max_sum = 0
    for i in range(0, min(K, N) + 1):
        for j in range(0, min(K - i, N - i) + 1):
            if i + j > N:
                continue
            else:
                sum = 0
                sum += sum_max(V[0:i])
                sum += sum_max(V[N - j:N])
                max_sum = max(max_sum, sum)
    return max_sum
