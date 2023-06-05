def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    print(c)
    for i in range(n):
        a.append(c[i][1:])
    print(a)
    min_cost = 99999999999999
    for i in range(2**n):
        cost = 0
        level = [0 for _ in range(m)]
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j][0]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x and cost < min_cost:
            min_cost = cost
    if min_cost == 99999999999999:
        print(-1)
    else:
        print(min_cost)
