def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    #print(c)
    #print(a)
    min_cost = 1000000000
    for i in range(2**n):
        cost = 0
        u = [0]*m
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    u[k] += a[j][k]
        if min(u) >= x:
            min_cost = min(min_cost, cost)
    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()