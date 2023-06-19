def solve():
    a,b = map(int,input().split())
    ans = 1e18
    for i in range(1,100000):
        t = 1 + (a + b * i) ** 0.5
        t = t / i
        ans = min(ans,t)
    print(ans)
solve()
