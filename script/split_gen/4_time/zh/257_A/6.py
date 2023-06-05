def getChar(N, X):
    if N == 1:
        return chr(X + 64)
    else:
        for i in range(1, 27):
            if X <= N * i:
                break
        return chr(64 + i) + getChar(N - 1, X - (i - 1) * N)
N, X = map(int, input().split())
print(getChar(N, X))
