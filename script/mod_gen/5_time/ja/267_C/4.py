def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i + 1]
    ans = 0
    for i in range(m):
        ans += a[i + 1] * (m - i)
    for i in range(n - m + 1):
        ans = max(ans, s[i + m] - s[i])
        for j in range(m):
            ans = max(ans, s[i + j] - s[i] + s[i + m] - s[i + j])
    print(ans)

if __name__ == '__main__':
    main()