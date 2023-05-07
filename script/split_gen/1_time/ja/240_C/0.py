def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X - b[i], -1, -1):
            if dp[j]:
                dp[j + b[i]] = True
                dp[j + a[i]] = True
    if dp[X]:
        print("Yes")
    else:
        print("No")
