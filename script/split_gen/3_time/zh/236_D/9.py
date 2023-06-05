def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([int(x) for x in input().split()])
    bit = [0] * (N+1)
    for i in range(N):
        for j in range(i+1, N):
            bit[i+1] ^= A[i][j]
    dp = [[0] * (1<<N) for _ in range(N+1)]
    for i in range(N):
        for j in range(1<<i):
            for k in range(i+1, N):
                if j & (1<<k):
                    dp[i+1][j] ^= A[i][k]
    ans = 0
    for i in range(N):
        for j in range(1<<N):
            if (j & (1<<i)) == 0:
                ans = max(ans, bit[i+1] ^ dp[i+1][j])
    print(ans)
