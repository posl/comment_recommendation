def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    min_cost = 10**5 * n + 1
    for i in range(2**n):
        cost = 0
        understanding = [0] * m
        for j in range(n):
            if ((i >> j) & 1):
                cost += c[j]
                for k in range(m):
                    understanding[k] += a[j][k]
        if all(x <= y for y in understanding):
            min_cost = min(min_cost, cost)
    if min_cost == 10**5 * n + 1:
        print(-1)
    else:
        print(min_cost)
