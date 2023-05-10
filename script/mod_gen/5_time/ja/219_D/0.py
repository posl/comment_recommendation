def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True
    for a, b in AB:
        for x in range(X-a, -1, -1):
            for y in range(Y-b, -1, -1):
                if dp[x][y]:
                    dp[x+a][y+b] = True
    ans = -1
    for x in range(X+1):
        for y in range(Y+1):
            if dp[x][y]:
                if ans == -1:
                    ans = x+y
                else:
                    ans = min(ans, x+y)
    print(ans)

if __name__ == '__main__':
    main()