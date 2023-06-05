def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    min_cost = 100000000
    for i in range(2**n):
        cost = 0
        understanding = [0 for j in range(m)]
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    understanding[k] += a[j][k]
        if min(understanding) >= x:
            min_cost = min(min_cost, cost)
    if min_cost == 100000000:
        print(-1)
    else:
        print(min_cost)
