def main():
    N, M = [int(x) for x in input().split()]
    AB = [[int(x) for x in input().split()] for _ in range(N)]
    AB.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * (M + 1)
    for i in range(N):
        a, b = AB[i]
        for j in range(M - a, -1, -1):
            dp[j + a] = max(dp[j + a], dp[j] + b)
    print(max(dp))
