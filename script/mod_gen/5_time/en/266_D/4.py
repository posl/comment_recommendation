def main():
    n = int(input())
    s = []
    for i in range(n):
        t, x, a = map(int, input().split())
        s.append([t, x, a])
    s.append([float('inf'), 0, 0])
    s.sort()
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i + 1])
        for j in range(i + 1, n + 1):
            if s[j][0] - s[i][0] >= abs(s[j][1] - s[i][1]):
                dp[j] = max(dp[j], dp[i] + s[j][2])
    print(dp[n])

if __name__ == '__main__':
    main()