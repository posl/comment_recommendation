def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(N-1):
            nxt = [0] * 10
            for k in range(10):
                nxt[(k + A[j]) % 10] += dp[k]
                nxt[(k * A[j]) % 10] += dp[k]
            dp = nxt
        ans[i] = dp[0]
    for i in range(10):
        print(ans[i])
