def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += x[i]
    for i in range(m):
        for j in range(n - c[i] + 1):
            tmp = 0
            for k in range(c[i]):
                tmp += x[j + k]
            ans = max(ans, tmp + y[i])
    print(ans)

if __name__ == '__main__':
    main()