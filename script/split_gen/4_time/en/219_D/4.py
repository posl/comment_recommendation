def main():
    N = int(input())
    X, Y = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    dp[min(x + A[i], X)][min(y + B[i], Y)] = True
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)
