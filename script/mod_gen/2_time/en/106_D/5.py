def main():
    N, M, Q = map(int, input().split())
    train = [[0]*(N+1) for i in range(N+1)]
    for i in range(M):
        L, R = map(int, input().split())
        train[L][R] += 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            train[i][j] += train[i][j-1] + train[i-1][j] - train[i-1][j-1]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q][q]-train[p-1][q]-train[q][p-1]+train[p-1][p-1])

if __name__ == '__main__':
    main()