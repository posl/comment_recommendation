def main():
    n, m, x = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    min_cost = -1
    for i in range(1<<n):
        cost = 0
        understand = [0]*m
        for j in range(n):
            if (i>>j)&1:
                cost += a[j][0]
                for k in range(m):
                    understand[k] += a[j][k+1]
        if min(understand) >= x:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)

if __name__ == '__main__':
    main()