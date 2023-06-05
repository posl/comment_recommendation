def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    # print(n, m, x)
    # print(c)
    # print(a)
    # print()
    import itertools
    min_cost = 10**9
    for i in range(1, n+1):
        for j in itertools.combinations(range(n), i):
            # print(j)
            temp_cost = 0
            temp_a = [0]*m
            for k in j:
                temp_cost += c[k]
                for l in range(m):
                    temp_a[l] += a[k][l]
            # print(temp_cost)
            # print(temp_a)
            # print()
            if min(temp_a) >= x:
                min_cost = min(min_cost, temp_cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()