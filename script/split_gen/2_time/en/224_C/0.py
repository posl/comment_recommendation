def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1 = X[i]
                y1 = Y[i]
                x2 = X[j]
                y2 = Y[j]
                x3 = X[k]
                y3 = Y[k]
                if (x1-x3)*(y2-y3) - (x2-x3)*(y1-y3) != 0:
                    ans += 1
    print(ans)
