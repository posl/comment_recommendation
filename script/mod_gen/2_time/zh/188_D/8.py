def main():
    n, c = map(int, input().split())
    a = []
    b = []
    cost = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        cost.append(c_i)
    #print(a)
    #print(b)
    #print(cost)
    min_cost = 0
    for i in range(n):
        min_cost += cost[i] * (b[i] - a[i] + 1)
    #print(min_cost)
    #print(c)
    #print(a)
    #print(b)
    min_cost += c
    #print(min_cost)
    #print(a)
    #print(b)
    #print(cost)
    for i in range(n - 1):
        if b[i] + 1 == a[i + 1]:
            min_cost -= cost[i] + cost[i + 1]
            if cost[i] > cost[i + 1]:
                min_cost -= cost[i + 1] * (b[i + 1] - a[i + 1] + 1)
                min_cost += cost[i] * (b[i + 1] - a[i + 1] + 1)
            #print(min_cost)
    print(min_cost)

if __name__ == '__main__':
    main()