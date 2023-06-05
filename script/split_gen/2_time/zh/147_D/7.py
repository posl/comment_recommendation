def get_honest_num(N, A, x, y):
    honest_num = 0
    for i in range(2 ** N):
        honest = []
        for j in range(N):
            if ((i >> j) & 1):
                honest.append(j + 1)
        honest_flag = True
        for j in range(N):
            if ((i >> j) & 1):
                for k in range(A[j]):
                    if (y[j][k] == 0):
                        if (x[j][k] not in honest):
                            honest_flag = False
                            break
                    else:
                        if (x[j][k] in honest):
                            honest_flag = False
                            break
            if (not honest_flag):
                break
        if (honest_flag):
            honest_num = max(honest_num, len(honest))
    return honest_num
