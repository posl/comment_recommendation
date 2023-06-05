def bouncing_ball(N, X, L):
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
        if D[i] > X:
            return i - 1
    return N
