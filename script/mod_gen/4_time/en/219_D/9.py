def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[False for _ in range(Y + 1)] for _ in range(X + 1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    if x + A[i] <= X and y + B[i] <= Y:
                        dp[x + A[i]][y + B[i]] = True
    ans = float('inf')
    for x in range(X, X + 301):
        for y in range(Y, Y + 301):
            if dp[x][y]:
                ans = min(ans, x + y)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()