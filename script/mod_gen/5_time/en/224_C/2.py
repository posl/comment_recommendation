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
                x1 = X[i] - X[k]
                y1 = Y[i] - Y[k]
                x2 = X[j] - X[k]
                y2 = Y[j] - Y[k]
                if x1 * y2 != x2 * y1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()