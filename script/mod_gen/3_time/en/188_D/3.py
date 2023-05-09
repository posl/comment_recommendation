def main():
    N, C = map(int, input().split())
    abcs = [tuple(map(int, input().split())) for _ in range(N)]
    abcs.sort(key=lambda x: x[1])
    dp = [0] * (abcs[-1][1] + 1)
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1]
        for j in range(N):
            if abcs[j][1] == i:
                dp[i] = min(dp[i], dp[abcs[j][0] - 1] + abcs[j][2])
    print(min(dp[-1], C * abcs[-1][1]))

if __name__ == '__main__':
    main()