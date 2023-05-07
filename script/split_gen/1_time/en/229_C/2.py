def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        A, B = map(int, input().split())
        cheese.append((A, B))
    cheese = sorted(cheese, key=lambda x: x[0])
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j + cheese[i][1] <= W:
                dp[j + cheese[i][1]] = max(dp[j + cheese[i][1]], dp[j] + cheese[i][0] * cheese[i][1])
            dp[j] = max(dp[j], dp[j + cheese[i][1] - W] + cheese[i][0] * (W - j))
    print(max(dp))
