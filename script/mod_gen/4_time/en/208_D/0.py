def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print(C)
    INF = 1000000000000000000
    d = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        d[i][i] = 0
    for i in range(M):
        d[A[i]][B[i]] = C[i]
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    #print(d)
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if d[i][j] == d[i][k] + d[k][j]:
                    ans += d[i][j]
    print(ans)

if __name__ == '__main__':
    main()