def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for _ in range(n)]
    ans = 10**9
    for i in range(n):
        for j in range(i+1,n):
            x1,y1 = xy[i]
            x2,y2 = xy[j]
            d = ((x1-x2)**2+(y1-y2)**2)**0.5
            if d < ans:
                ans = d
    print(ans)
solve()
