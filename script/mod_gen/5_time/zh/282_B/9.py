def solve():
    n,m=map(int,input().split())
    s=[]
    for i in range(n):
        s.append(input())
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ok=True
            for k in range(m):
                if s[i][k]!='o' and s[j][k]!='o':
                    ok=False
            if ok:
                ans+=1
    print(ans)
solve()
