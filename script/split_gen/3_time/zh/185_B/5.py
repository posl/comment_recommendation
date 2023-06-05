def solve():
    n,m,t = map(int,input().split())
    ans = n
    for i in range(m):
        a,b = map(int,input().split())
        ans += a - b
        if ans <= 0:
            print("No")
            return
        if ans >= n:
            ans = n
    ans += t - b
    if ans <= 0:
        print("No")
        return
    print("Yes")
solve()
