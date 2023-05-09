def main():
    n, w = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese.sort(key=lambda x: x[1])
    dp = [0] * (w + 1)
    for a, b in cheese:
        for i in range(w, b - 1, -1):
            dp[i] = max(dp[i], dp[i - b] + a)
    print(dp[w])
