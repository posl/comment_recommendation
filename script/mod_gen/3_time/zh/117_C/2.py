def findMinMoves(N, M, X):
    X.sort()
    if M == 1:
        return 0
    else:
        sum = 0
        for i in range(M - 1):
            sum += X[i + 1] - X[i]
        if N == 1:
            return sum
        else:
            return sum - min(X[1] - X[0], X[M - 1] - X[M - 2])

if __name__ == '__main__':
    findMinMoves()