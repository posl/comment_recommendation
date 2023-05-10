def main():
    n,m,x=map(int,input().split())
    c=[]
    a=[]
    for i in range(n):
        tmp=list(map(int,input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    #print(c)
    #print(a)
    min_cost=1000000
    for i in range(2**n):
        #print(i)
        cost=0
        understanding=[0]*m
        for j in range(n):
            if ((i>>j)&1):
                cost+=c[j]
                for k in range(m):
                    understanding[k]+=a[j][k]
        #print(understanding)
        if (min(understanding)>=x):
            min_cost=min(min_cost,cost)
    if (min_cost==1000000):
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()