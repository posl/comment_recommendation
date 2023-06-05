def get_min_cost(N, M, X, C, A):
    min_cost = -1
    for i in range(1, 2 ** N):
        cost = 0
        algos = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    algos[k] += A[j][k]
        if min(algos) >= X:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    return min_cost
