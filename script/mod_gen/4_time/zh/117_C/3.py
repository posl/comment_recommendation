def findMinStep(N, M, X):
    import bisect
    X.sort()
    if M == 1:
        return 0
    if M == 2:
        return min(abs(X[0]-X[1]), X[1]-X[0])
    if X[0] >= 0:
        return X[-1] - X[0]
    if X[-1] <= 0:
        return abs(X[0] - X[-1])
    if X[0] < 0 and X[-1] > 0:
        pos = bisect.bisect_left(X, 0)
        if pos == 0:
            return abs(X[0]) + X[-1]
        if pos == M:
            return X[-1] - abs(X[-1])
        if pos >= 1 and pos <= M-1:
            return min(abs(X[0]), abs(X[-1]))*2 + max(abs(X[0]), abs(X[-1]))
    return 0

if __name__ == '__main__':
    findMinStep()