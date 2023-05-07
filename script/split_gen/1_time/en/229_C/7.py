def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0])
    INF = 10**9+7
    dp = [INF] * (W+1)
    dp[0] = 0
    for a, b in cheese:
        for i in range(W):
            if i+a <= W:
                dp[i+a] = min(dp[i+a], dp[i]+b)
    print(max([a*b for a, b in cheese if b <= dp[W]]))
