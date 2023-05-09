def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    C = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j]
            if i > 0:
                C[i][j] += C[i - 1][j]
            if j > 0:
                C[i][j] += C[i][j - 1]
            if i > 0 and j > 0:
                C[i][j] -= C[i - 1][j - 1]
    ans = 10 ** 9 + 1
    for i in range(K - 1, N):
        for j in range(K - 1, N):
            cnt = C[i][j]
            if i - K >= 0:
                cnt -= C[i - K][j]
            if j - K >= 0:
                cnt -= C[i][j - K]
            if i - K >= 0 and j - K >= 0:
                cnt += C[i - K][j - K]
            ans = min(ans, cnt)
    print(ans // (K * K))

if __name__ == '__main__':
    main()