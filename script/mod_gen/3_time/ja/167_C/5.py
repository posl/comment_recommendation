def main():
    n, m, x = map(int, input().split())
    c = [0] * n
    a = [[0] * m for i in range(n)]
    for i in range(n):
        c[i], *a[i] = map(int, input().split())
    ans = 10**9 + 1
    for i in range(2**n):
        cost = 0
        level = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, cost)
    if ans == 10**9 + 1:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()