def solve():
    N, M = map(int, input().split())
    N2 = N ** 2
    M2 = M ** 2
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if ans[k][l] != -1:
                        continue
                    if (i - k) ** 2 + (j - l) ** 2 == M2:
                        ans[k][l] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])
solve()
