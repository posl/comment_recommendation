def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #print(X)
    #print(Y)
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                #print(i, j, k)
                #print(X[i], Y[i])
                #print(X[j], Y[j])
                #print(X[k], Y[k])
                #print((X[j] - X[i]) * (Y[k] - Y[i]) - (X[k] - X[i]) * (Y[j] - Y[i]))
                if (X[j] - X[i]) * (Y[k] - Y[i]) - (X[k] - X[i]) * (Y[j] - Y[i]) != 0:
                    cnt += 1
    print(cnt)
