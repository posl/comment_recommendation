def check_honesty(N, A, x, y):
    honest = 0
    for i in range(N):
        if A[i] == 0:
            honest += 1
            continue
        else:
            honest_count = 0
            for j in range(A[i]):
                if y[i][j] == 1 and A[x[i][j]-1] > 0:
                    honest_count += 1
            if honest_count == A[i]:
                honest += 1
    return honest
