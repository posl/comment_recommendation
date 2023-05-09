def main():
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(N)]
    # 1日目から最終日までのすぬけプライムの有無を格納するリスト
    # 1日目から最終日までのすぬけプライムの有無を格納するリスト
    dp = [0] * (10 ** 9 + 1)
    for i in range(N):
        a, b, c = abc[i]
        dp[a] += c
        dp[b + 1] -= c
    for i in range(1, 10 ** 9 + 1):
        dp[i] += dp[i - 1]
    ans = 0
    for i in range(1, 10 ** 9 + 1):
        ans += min(dp[i], C)
    print(ans)
