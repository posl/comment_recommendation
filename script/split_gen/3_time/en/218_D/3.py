def main():
    N = int(input())
    XY = [list(map(int, input().split())) for i in range(N)]
    X = [XY[i][0] for i in range(N)]
    Y = [XY[i][1] for i in range(N)]
    X.sort()
    Y.sort()
    X = list(set(X))
    Y = list(set(Y))
    X = [X.index(XY[i][0]) for i in range(N)]
    Y = [Y.index(XY[i][1]) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if X[i] == X[j]:
                continue
            for k in range(N):
                if Y[k] == Y[i] or Y[k] == Y[j]:
                    continue
                if X[i] < X[k] and X[k] < X[j] and Y[i] < Y[k] and Y[k] < Y[j]:
                    ans += 1
    print(ans)
