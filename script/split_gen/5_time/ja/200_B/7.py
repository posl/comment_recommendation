def solve(N, K):
    for i in range(K):
        if N%200==0:
            N = N//200
        else:
            N = int(str(N) + "200")
    return N
