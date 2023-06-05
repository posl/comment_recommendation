def check_honesty(honesty, N, A, x, y):
    for i in range(N):
        if honesty[i] == 1:
            for j in range(A[i]):
                if y[i][j] == 1 and honesty[x[i][j]-1] == 0:
                    return False
                if y[i][j] == 0 and honesty[x[i][j]-1] == 1:
                    return False
    return True

if __name__ == '__main__':
    check_honesty()