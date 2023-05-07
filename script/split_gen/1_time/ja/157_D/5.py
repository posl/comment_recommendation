def solve():
    n,m,k=map(int,input().split())
    friend=set()
    block=set()
    for _ in range(m):
        a,b=map(int,input().split())
        friend.add((a,b))
        friend.add((b,a))
    for _ in range(k):
        c,d=map(int,input().split())
        block.add((c,d))
        block.add((d,c))
    ans=[0]*n
    for i in range(n):
        for j in range(1,n+1):
            if i+1==j:
                continue
            if (i+1,j) in block:
                continue
            if (i+1,j) in friend:
                continue
            if (j,i+1) in friend:
                continue
            ans[i]+=1
    print(*ans)
