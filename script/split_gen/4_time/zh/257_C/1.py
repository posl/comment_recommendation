def f(x, N, S, W):
    res = 0
    for i in range(N):
        if S[i] == '0' and W[i] < x:
            res += 1
        elif S[i] == '1' and W[i] >= x:
            res += 1
    return res
