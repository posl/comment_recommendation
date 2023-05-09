def main():
    N = int(input())
    T = [0] + [int(input().split()[0]) for _ in range(N)]
    A = [list(map(int, input().split()[1:])) for _ in range(N)]
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = T[i] + max(dp[j] for j in A[i - 1])
    print(dp[-1])
