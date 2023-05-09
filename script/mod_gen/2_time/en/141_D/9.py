def get_min_cost(n, m, a):
    a.sort(reverse=True)
    cost = 0
    for i in range(n):
        cost += a[i]
        if i < m:
            cost -= a[i] // 2
    return cost

if __name__ == '__main__':
    get_min_cost()