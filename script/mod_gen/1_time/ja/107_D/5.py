def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = [0] * n
    for i in range(n):
        c[i] = b[i // 2]
        if i % 2 == 1:
            c[i] = -c[i]
    d = [0] * n
    for i in range(n):
        d[i] = c[i] + d[i - 1]
    e = [0] * n
    for i in range(n):
        e[i] = a[i] + e[i - 1]
    ans = 0
    for i in range(n):
        ans += (i + 1) * a[i] - e[i]
        ans += (n - i - 1) * a[i] - (e[n - 1] - e[i])
        ans += d[i] * a[i]
        ans -= (d[i] - d[0]) * a[i]
    print(ans)

if __name__ == '__main__':
    main()