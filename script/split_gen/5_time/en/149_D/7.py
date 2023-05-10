def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # 0:G, 1:C, 2:P
    hands = {'r': 0, 's': 1, 'p': 2}
    # 0:G, 1:C, 2:P
    scores = [P, R, S]
    # 0:G, 1:C, 2:P
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    for i in range(N):
        for j in range(3):
            if i < K or dp[i-K][(j+1)%3] < dp[i-K][(j+2)%3]:
                dp[i+1][j] = dp[i][j] + scores[j] * (1 if hands[T[i]] == j else 0)
            else:
                dp[i+1][j] = dp[i-K][j] + scores[j] * (1 if hands[T[i]] == j else 0)
    print(max(dp[N]))
