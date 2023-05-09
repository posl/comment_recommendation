def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    AB = [AB[i] for i in range(N) if AB[i][0] <= M]
    N = len(AB)
    dp = [0] * (N+1)
    for i in range(N):
        dp[i+1] = max(dp[i], dp[i] + AB[i][1])
    print(dp[N])
