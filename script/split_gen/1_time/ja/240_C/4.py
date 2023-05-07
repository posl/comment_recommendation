def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j]:
                if j + A[i] <= X:
                    dp[j + A[i]] = True
                if j + B[i] <= X:
                    dp[j + B[i]] = True
    if dp[X]:
        print('Yes')
    else:
        print('No')
