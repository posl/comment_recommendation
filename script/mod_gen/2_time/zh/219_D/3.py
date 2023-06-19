def solve():
    n = int(input())
    x, y = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[float('inf')] * (y+1) for _ in range(x+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(x,-1,-1):
            for k in range(y,-1,-1):
                if dp[j][k] != float('inf'):
                    dp[min(x,j+A[i])][min(y,k+B[i])] = min(dp[min(x,j+A[i])][min(y,k+B[i])],dp[j][k]+1)
    if dp[x][y] == float('inf'):
        print(-1)
    else:
        print(dp[x][y])

if __name__ == '__main__':
    solve()