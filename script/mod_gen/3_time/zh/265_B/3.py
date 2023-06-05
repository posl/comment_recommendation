def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x.append(list(map(int,input().split())))
        y.append(x[i][1])
        x[i] = x[i][0]
    #print(n,m,t,a,x,y)
    #print(a)
    #print(x)
    #print(y)
    now = 1
    nowt = t
    for i in range(n-1):
        #print(i)
        #print(now)
        #print(nowt)
        #print(a[i])
        nowt -= a[i]
        if nowt <= 0:
            print('No')
            return
        if now == x[0]:
            nowt += y[0]
            x.pop(0)
            y.pop(0)
            if len(x) == 0:
                print('Yes')
                return
        now += 1
    print('No')
    return

if __name__ == '__main__':
    main()