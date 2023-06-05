def cal_times(A,B,K):
    times = 0
    while A < B:
        A = A * K
        times += 1
    return times
