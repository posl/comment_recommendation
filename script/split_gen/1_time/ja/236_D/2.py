def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [0] * (2 ** N)
    for i in range(2 ** N):
        for j in range(N):
            if ((i >> j) & 1):
                B[i] ^= A[j][i & ((1 << j) - 1)]
    dp = [0] * (2 ** N)
    for i in range(2 ** N):
        for j in range(2 ** N):
            if ((i & j) == 0):
                dp[i | j] = max(dp[i | j], dp[i] + B[j])
    print(dp[-1])
