def solve():
    N,M,X=map(int,input().split())
    l=[]
    for i in range(N):
        l.append(list(map(int,input().split())))
    #print(l)
    cost=0
    min_cost=-1
    for i in range(2**N):
        cost=0
        level=[0]*M
        for j in range(N):
            if ((i>>j)&1):
                cost+=l[j][0]
                for k in range(M):
                    level[k]+=l[j][k+1]
        #print(cost,level)
        if min(level)>=X:
            if min_cost==-1:
                min_cost=cost
            elif min_cost>cost:
                min_cost=cost
    print(min_cost)
solve()
