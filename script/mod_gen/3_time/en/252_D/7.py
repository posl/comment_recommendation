def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    from collections import Counter
    counter = Counter(A)
    if any([v >= 3 for v in counter.values()]):
        print(0)
        return
    # dp[i][j] = i番目までの数を使って、j個の数字を使った場合の組み合わせの数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= 1:
                dp[i][j] += dp[i - 1][j - 1]
    ans = 0
    for i in range(1, N + 1):
        ans += dp[N][i] * i
    print(ans)

if __name__ == '__main__':
    solve()