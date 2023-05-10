def min_cost(N, K, X, A):
    cost = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                cost += X
                K -= 1
            else:
                cost += A[i]
        else:
            cost += A[i]
    return cost
