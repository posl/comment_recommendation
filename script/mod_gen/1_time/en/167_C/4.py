def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    #print(n, m, x)
    #print(c)
    #print(a)
    #print('----')
    cost = 10**9
    for i in range(2**n):
        #print('i:', i)
        tmp = [0 for _ in range(m)]
        tmp_cost = 0
        for j in range(n):
            if ((i >> j) & 1):
                tmp_cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        #print(tmp)
        #print(tmp_cost)
        #print('----')
        flag = True
        for j in range(m):
            if tmp[j] < x:
                flag = False
        if flag:
            cost = min(cost, tmp_cost)
    if cost == 10**9:
        print(-1)
    else:
        print(cost)

if __name__ == '__main__':
    main()