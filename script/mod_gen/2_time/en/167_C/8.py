def solve():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**9+1
    for bit in range(1 << N):
        cost = 0
        level = [0] * M
        for i in range(N):
            if (bit >> i) & 1:
                cost += A[i][0]
                for j in range(M):
                    level[j] += A[i][j+1]
        if min(level) >= X:
            ans = min(ans, cost)
    if ans == 10**9+1:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()