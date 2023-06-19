def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort(key=lambda x: x[0])
    # print(ABC)
    # dp = [0] * (10**9 + 1)
    dp = [0] * (10**9 + 1)
    dp[0] = 0
    for i in range(1, ABC[-1][1] + 1):
        dp[i] = dp[i-1] + C
        for j in range(N):
            if i >= ABC[j][0]:
                dp[i] = min(dp[i], dp[ABC[j][0]] + ABC[j][2] + (i - ABC[j][0]) * ABC[j][1])
    print(dp[ABC[-1][1]])

if __name__ == '__main__':
    main()