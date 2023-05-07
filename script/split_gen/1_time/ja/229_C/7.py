def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1])
    dp = [0]*(W+1)
    for a, b in cheese:
        for i in range(W, -1, -1):
            if i+b <= W:
                dp[i+b] = max(dp[i+b], dp[i]+a)
    print(max(dp))
