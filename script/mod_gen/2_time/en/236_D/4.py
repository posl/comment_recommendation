def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for _ in range(1 << N)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(i + 1, N):
            dp[2][1 << i | 1 << j] = A[i][j]
    for i in range(3, N + 1):
        for bit in range(1 << N):
            if bin(bit).count('1') != i:
                continue
            for j in range(N):
                if not bit & 1 << j:
                    continue
                for k in range(j + 1, N):
                    if not bit & 1 << k:
                        continue
                    dp[i][bit] = max(dp[i][bit], dp[i - 1][bit ^ 1 << j ^ 1 << k] + A[j][k])
    print(dp[N][(1 << N) - 1])

if __name__ == '__main__':
    solve()