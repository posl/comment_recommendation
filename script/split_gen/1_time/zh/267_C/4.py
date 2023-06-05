def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = -10**18
    for i in range(m + 1):
        for j in range(m + 1 - i):
            if i + 2 * j > m:
                continue
            t = s[i] + (s[n] - s[n - j]) + (s[n - j] - s[n - j - i])
            ans = max(ans, t)
    print(ans)
main()
