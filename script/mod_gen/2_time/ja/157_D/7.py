def main():
    N, M, K = map(int, input().split())
    F = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        F[a-1][b-1] = F[b-1][a-1] = 1
    B = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        c, d = map(int, input().split())
        B[c-1][d-1] = B[d-1][c-1] = 1
    ans = [0]*N
    for i in range(N):
        for j in range(i+1, N):
            if F[i][j] == 1:
                ans[i] += 1
                ans[j] += 1
    for i in range(N):
        for j in range(N):
            if B[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        ans[i] = N - ans[i] - 1
    print(*ans)

if __name__ == '__main__':
    main()