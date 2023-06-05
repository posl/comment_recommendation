def max_num(N,S,W):
    max_num = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] > max_num:
                max_num = W[i]
    return max_num
