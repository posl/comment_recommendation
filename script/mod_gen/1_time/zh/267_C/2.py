def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i] + i * a[i]
    d = [0] * (n + 1)
    for i in range(n):
        d[i + 1] = d[i] + a[i] * (i + 1) * (n - i)
    ans = 0
    for i in range(m, n + 1):
        ans = max(ans, b[i] * i - (c[i] - c[i - m]) - (d[n] - d[i]))
    print(ans)

if __name__ == '__main__':
    main()