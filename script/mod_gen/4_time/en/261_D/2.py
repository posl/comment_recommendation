def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    ans = 0
    for i in range(n):
        ans += x[i]
    for i in range(m):
        min = 10**9
        for j in range(n):
            if c[i] <= j + 1:
                if min > x[j] - y[i] * (j + 1 - c[i]):
                    min = x[j] - y[i] * (j + 1 - c[i])
        if min > 0:
            ans -= min
    print(ans)

if __name__ == '__main__':
    main()