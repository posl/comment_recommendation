def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j] and j + A[i] <= X:
                dp[j + A[i]] = True
            if dp[j] and j + B[i] <= X:
                dp[j + B[i]] = True
    if dp[X]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()