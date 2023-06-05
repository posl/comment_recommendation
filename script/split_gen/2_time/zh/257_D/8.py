def f(x, N, S, W):
    count = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] < x:
                count += 1
        else:
            if W[i] >= x:
                count += 1
    return count
