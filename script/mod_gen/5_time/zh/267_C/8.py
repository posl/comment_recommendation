def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(n + 1):
        if i % m == 0:
            l[i] = s[i]
        else:
            l[i] = max(l[i - 1], s[i])
    for i in range(n, -1, -1):
        if i % m == 0:
            r[i] = s[i]
        else:
            r[i] = max(r[i + 1], s[i])
    ans = 0
    for i in range(1, n):
        ans = max(ans, l[i] + r[i + 1] - s[i])
    print(ans)

if __name__ == '__main__':
    main()