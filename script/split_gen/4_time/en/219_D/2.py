def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = True
    for i in range(1, N+1):
        for x in range(X+1):
            for y in range(Y+1):
                if dp[i-1][x][y]:
                    dp[i][x][y] = True
                    if x+A[i-1] <= X and y+B[i-1] <= Y:
                        dp[i][x+A[i-1]][y+B[i-1]] = True
    ans = -1
    for i in range(1, N+1):
        if dp[i][X][Y]:
            ans = i
            break
    print(ans)
