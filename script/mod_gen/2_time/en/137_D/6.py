def solve():
    N, M = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB = sorted(AB, key=lambda x: x[0])
    AB = sorted(AB, key=lambda x: x[1], reverse=True)
    dp = [0] * (M + 1)
    for a, b in AB:
        for i in range(M, -1, -1):
            if i + a <= M:
                dp[i + a] = max(dp[i + a], dp[i] + b)
    print(max(dp))

if __name__ == '__main__':
    solve()