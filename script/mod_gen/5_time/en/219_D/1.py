def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False] * (Y + 1) for i in range(X + 1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y] and x + A[i] <= X and y + B[i] <= Y:
                    dp[x + A[i]][y + B[i]] = True
    ans = -1
    for x in range(X + 1):
        for y in range(Y + 1):
            if dp[x][y]:
                ans = max(ans, x + y)
    print(ans)

if __name__ == '__main__':
    solve()