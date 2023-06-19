def solve():
    n,m=map(int,input().split())
    edge=[]
    for _ in range(m):
        u,v=map(int,input().split())
        edge.append((u,v))
    edge.sort()
    ans=0
    cnt=1
    for i in range(1,m):
        if edge[i]==edge[i-1]:
            cnt+=1
        else:
            ans+=cnt*(cnt-1)//2
            cnt=1
    ans+=cnt*(cnt-1)//2
    print(n*(n-1)//2-ans)

if __name__ == '__main__':
    solve()