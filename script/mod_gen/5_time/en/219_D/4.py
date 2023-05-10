def lunchbox():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False]*(Y+1) for _ in range(X+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if dp[j][k]:
                    dp[min(X, j+A[i])][min(Y, k+B[i])] = True
    ans = -1
    for i in range(X+1):
        for j in range(Y+1):
            if dp[i][j]:
                ans = i+j
    return ans
print(lunchbox())

if __name__ == '__main__':
    lunchbox()