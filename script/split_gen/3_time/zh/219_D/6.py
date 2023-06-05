def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(301)] for j in range(301)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(300, -1, -1):
            for k in range(300, -1, -1):
                if dp[j][k] == 1:
                    dp[j + A[i]][k + B[i]] = 1
    ans = -1
    for i in range(X, 301):
        for j in range(Y, 301):
            if dp[i][j] == 1:
                ans = i + j
                break
        if ans != -1:
            break
    print(ans)
