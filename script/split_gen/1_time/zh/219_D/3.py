def solve():
    n = int(input())
    x,y = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    ans = -1
    for i in range(n):
        if a[i]>=x and b[i]>=y:
            ans = 1
            break
    if ans == -1:
        print(-1)
    else:
        for i in range(n):
            if a[i]>=x and b[i]>=y:
                ans = min(ans,a[i]+b[i])
        print(ans)
