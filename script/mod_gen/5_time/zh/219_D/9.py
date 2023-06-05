def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    dp = [[0]*(Y+1) for _ in range(X+1)]
    dp[0][0] = 1
    ans = 10**9
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j]:
                    dp[min(X, i+a)][min(Y, j+b)] = 1
                    if i+a >= X and j+b >= Y:
                        ans = min(ans, dp[i][j]+1)
    print(ans if ans != 10**9 else -1)

if __name__ == '__main__':
    main()