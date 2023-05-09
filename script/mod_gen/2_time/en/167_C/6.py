def main():
    n, m, x = map(int, input().split())
    c = [0] * n
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        c[i] = tmp[0]
        for j in range(m):
            a[i][j] = tmp[j + 1]
    ans = 10 ** 9
    for i in range(2 ** n):
        tmp = [0] * m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        if all([x <= t for t in tmp]):
            ans = min(ans, cost)
    if ans == 10 ** 9:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()