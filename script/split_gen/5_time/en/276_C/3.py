def solve():
    n=int(input())
    p=list(map(int,input().split()))
    p.insert(0,0)
    q=[0]*(n+1)
    for i in range(1,n+1):
        q[p[i]]=i
    print(*q[1:])
solve()
