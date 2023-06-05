def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i],y[i] = map(int,input().split())
    ans = 10**18
    for i in range(n):
        for j in range(i+1,n):
            for l in range(n):
                if l in a:
                    ans = min(ans,max((x[i]-x[l])**2+(y[i]-y[l])**2,(x[j]-x[l])**2+(y[j]-y[l])**2)**0.5)
    print(ans)
solve()
