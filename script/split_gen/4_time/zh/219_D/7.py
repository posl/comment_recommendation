def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    dp = [[[False for k in range(Y+1)] for j in range(X+1)] for i in range(N+1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j+A[i]<=X and k+B[i]<=Y:
                        dp[i+1][j+A[i]][k+B[i]] = True
    #print(dp)
    if dp[N][X][Y]:
        for i in range(N, 0, -1):
            if dp[i-1][X][Y]:
                continue
            else:
                print(i)
                break
    else:
        print(-1)
main()
