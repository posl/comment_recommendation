def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False for i in range(X+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X+1):
            for k in range(B[i]+1):
                if j >= A[i] * k and dp[i][j - A[i] * k]:
                    dp[i+1][j] = True
    if dp[N][X]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()