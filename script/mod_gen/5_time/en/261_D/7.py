def solve(N, M, X, C, Y):
    result = 0
    for i in range(0, N):
        if X[i] == 1:
            result += Y[0]
        elif X[i] == 2:
            result += Y[1]
        elif X[i] == 3:
            result += Y[2]
        else:
            result += Y[3]
    return result

if __name__ == '__main__':
    solve()