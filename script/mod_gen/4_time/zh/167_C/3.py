def get_min_cost(n, m, x, c, a):
    min_cost = -1
    for i in range(1, 1 << n):
        cost = 0
        u = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    u[k] += a[j][k]
        if all(x <= ui for ui in u):
            if min_cost == -1 or cost < min_cost:
                min_cost = cost
    return min_cost

if __name__ == '__main__':
    get_min_cost()