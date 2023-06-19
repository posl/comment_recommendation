def cal_f(x):
    f = 0
    for i in range(N):
        if S[i] == '0' and W[i] < x:
            f += 1
        elif S[i] == '1' and W[i] >= x:
            f += 1
    return f
