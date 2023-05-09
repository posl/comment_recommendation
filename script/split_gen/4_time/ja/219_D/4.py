def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j]:
                    if i+a <= X and j+b <= Y:
                        dp[i+a][j+b] = True
    ans = -1
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                ans = i+j
                break
        if ans > 0:
            break
    print(ans)
