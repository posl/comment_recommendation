def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    d = [0] * (n + 1)
    e = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    for i in range(n):
        c[i + 1] = c[i] + b[i]
    for i in range(n):
        d[i + 1] = d[i] + c[i]
    for i in range(n):
        e[i + 1] = e[i] + d[i]
    ans = 10 ** 18
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                p = b[i]
                q = c[j] - c[i]
                r = d[k] - d[j]
                s = e[n] - e[k]
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)

if __name__ == '__main__':
    solve()