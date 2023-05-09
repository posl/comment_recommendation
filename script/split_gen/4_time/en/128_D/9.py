def max_jewels(N, K, V):
    max_sum = 0
    for i in range(1, min(N, K) + 1):
        for j in range(i + 1):
            s = sorted(V[:j] + V[N - (i - j):])
            max_sum = max(max_sum, sum(s[i:]))
    return max_sum
