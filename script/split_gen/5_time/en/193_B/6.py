def buy_play_snuke(N, A, P, X):
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1:
                result = P[i]
            else:
                result = min(result, P[i])
    return result
