def calc_time(N, M, T, A, XY):
    for i in range(M):
        X = XY[i][0]
        Y = XY[i][1]
        if T < X:
            return False
        T += Y
    for i in range(N-1):
        T -= A[i]
        if T <= 0:
            return False
    return True

if __name__ == '__main__':
    calc_time()