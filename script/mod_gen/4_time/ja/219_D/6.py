def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: (x[0], x[1]))
    dp = [[0 for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = 1
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j] == 0:
                    continue
                if i + a <= X and j + b <= Y:
                    dp[i+a][j+b] = 1
    ans = 0
    for i in range(X+1):
        for j in range(Y+1):
            if dp[i][j] == 1:
                ans = max(ans, i+j)
    if ans == 0:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()