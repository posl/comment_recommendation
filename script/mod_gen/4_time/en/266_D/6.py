def main():
    n = int(input())
    snukes = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snukes.append((t, x, a))
    snukes.sort(key=lambda x: x[0])
    dp = [0] * 5
    for t, x, a in snukes:
        dp[x] = max(dp[x], max(dp[:x]) + a)
    print(max(dp))

if __name__ == '__main__':
    main()