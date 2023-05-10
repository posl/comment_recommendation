def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))
    roads.sort()
    roads.append((n, n))
    dp = [0] * n
    dp[0] = 1
    i = 0
    for j in range(m):
        if roads[j][0] != roads[j + 1][0]:
            while i < j + 1:
                dp[roads[i][1] - 1] += dp[roads[i][0] - 1]
                dp[roads[i][1] - 1] %= 10 ** 9 + 7
                i += 1
    print(dp[-1])

if __name__ == '__main__':
    main()