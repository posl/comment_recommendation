def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [0] * (w + 1)
    for i in range(n):
        for j in range(w, 0, -1):
            if j >= b[i]:
                dp[j] = max(dp[j], dp[j - b[i]] + a[i])
    print(dp[w])

if __name__ == '__main__':
    main()