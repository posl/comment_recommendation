def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    ans = 10**9
    for i in range(1 << n):
        cost = 0
        level = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
main()

if __name__ == '__main__':
    main()