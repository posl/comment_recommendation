def solve():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == n:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
solve()
