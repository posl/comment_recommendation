def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #print(N, K)
    #print(A)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                #print(i, j, k)
                x1 = X[i]
                y1 = Y[i]
                x2 = X[j]
                y2 = Y[j]
                x3 = X[k]
                y3 = Y[k]
                #print(x1, y1, x2, y2, x3, y3)
                ans = max(ans, solve(x1, y1, x2, y2, x3, y3))
    print(ans)
    return
