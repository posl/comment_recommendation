def max_sum(N, K, V):
    if K == 0:
        return 0
    if N == 1:
        return V[0]
    if N == 2:
        return max(V[0], V[1])
    if N == 3:
        return max(V[0] + V[2], V[1])
    if N == 4:
        return max(V[0] + V[2], V[1] + V[3])
    if N == 5:
        return max(V[0] + V[2] + V[4], V[1] + V[3])
    if N == 6:
        return max(V[0] + V[2] + V[4], V[1] + V[3] + V[5])
