def main():
    n, c = map(int, input().split())
    abcs = [list(map(int, input().split())) for _ in range(n)]
    abcs.sort(key=lambda x: x[0])
    abcs.sort(key=lambda x: x[1])
    dp = [0] * (abcs[-1][1] + 1)
    for i in range(n):
        a, b, c = abcs[i]
        dp[b] = max(dp[b], dp[a - 1] + c)
    for i in range(1, len(dp)):
        dp[i] = max(dp[i], dp[i - 1])
    print(sum([c for a, b, c in abcs]) - min(dp))

if __name__ == '__main__':
    main()