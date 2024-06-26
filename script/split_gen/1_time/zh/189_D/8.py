def calc(x):
    y = [0] * (N + 1)
    y[0] = x[0]
    for i in range(1, N + 1):
        if S[i - 1] == 'AND':
            y[i] = y[i - 1] and x[i]
        else:
            y[i] = y[i - 1] or x[i]
    return y[N]
