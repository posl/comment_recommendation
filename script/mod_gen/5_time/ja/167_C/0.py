def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_, *a_ = map(int, input().split())
        c.append(c_)
        a.append(a_)
    ans = float('inf')
    for i in range(1 << n):
        cost = 0
        u = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    u[k] += a[j][k]
        if all(v >= x for v in u):
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()