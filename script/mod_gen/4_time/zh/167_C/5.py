def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(c)
    print(a)
    for i in range(n):
        for j in range(m):
            a[i][j] += c[i][0]
    print(a)
    # for i in range(n):
    #     for j in range(m):
    #         print(a[i][j])
    ans = 100000000
    for i in range(2**n):
        cost = 0
        level = [0]*m
        for j in range(n):
            if (i>>j)&1:
                cost += c[j][0]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans,cost)
    if ans == 100000000:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()