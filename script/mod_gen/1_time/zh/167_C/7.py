def main():
    n, m, x = map(int, input().split())
    a = []
    c = []
    for i in range(n):
        c_i, *a_i = map(int, input().split())
        a.append(a_i)
        c.append(c_i)
    min_cost = 10 ** 9
    for i in range(1 << n):
        cost = 0
        understanding = [0] * m
        for j in range(n):
            if i >> j & 1:
                for k in range(m):
                    understanding[k] += a[j][k]
                cost += c[j]
        if all(x <= u for u in understanding):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost < 10 ** 9 else -1)

if __name__ == '__main__':
    main()