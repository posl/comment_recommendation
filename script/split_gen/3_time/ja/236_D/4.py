def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    B = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            B[i] ^= A[j][i]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(1 << N):
            if dp[i][j] == 1:
                dp[i + 1][j] = 1
                dp[i + 1][j ^ B[i]] = 1
    print((1 << N) - dp[-1][-1])
