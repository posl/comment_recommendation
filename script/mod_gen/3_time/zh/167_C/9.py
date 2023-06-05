def get_min_cost(N, M, X, C, A):
    min_cost = -1
    for i in range(1, 1<<N):
        cost = 0
        understand = [0 for _ in range(M)]
        for j in range(N):
            if (i>>j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            if min_cost == -1 or cost < min_cost:
                min_cost = cost
    return min_cost

if __name__ == '__main__':
    get_min_cost()