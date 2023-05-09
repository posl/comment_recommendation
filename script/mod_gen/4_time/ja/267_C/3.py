def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    c = [0] * (n+1)
    d = 0
    for i in range(n):
        d = max(d, b[i+1])
        c[i+1] = d
    e = [0] * (n+1)
    f = 0
    for i in range(n+1):
        f = max(f, b[i])
        e[i] = f
    ans = 0
    for i in range(1, n+1):
        if i >= m:
            ans = max(ans, c[i-m] + e[i])
    print(ans)

if __name__ == '__main__':
    main()