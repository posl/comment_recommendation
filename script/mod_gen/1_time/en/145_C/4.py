def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    D = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            D[i][j] = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** 0.5
    #print(D)
    p = list(range(N))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            p[i], p[j] = p[j], p[i]
            #print(p)
            tmp = 0
            for k in range(N - 1):
                tmp += D[p[k]][p[k + 1]]
            ans += tmp
            p[i], p[j] = p[j], p[i]
    print(ans * 2 / math.factorial(N))

if __name__ == '__main__':
    main()