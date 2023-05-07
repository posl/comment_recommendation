def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (W+1)
    dp[0] = 1
    ans = 0
    for i in range(N):
        for j in range(W, A[i]-1, -1):
            dp[j] |= dp[j-A[i]]
        ans += dp.count(1)
    print(ans)
