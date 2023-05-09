def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j]:
                dp[j + a[i]] = True
                dp[j + b[i]] = True
    if dp[X]:
        print('Yes')
    else:
        print('No')
