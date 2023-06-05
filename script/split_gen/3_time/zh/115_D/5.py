def main():
    n,x = map(int, input().split())
    dp = [0] * (n+1)
    p = [0] * (n+1)
    dp[0] = 1
    p[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * 2 + 1
        p[i] = p[i-1] * 2 + 3
    def f(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        elif x <= 1 + dp[n-1]:
            return f(n-1, x-1)
        else:
            return p[n-1] + 1 + f(n-1, x - 2 - dp[n-1])
    print(f(n,x))
