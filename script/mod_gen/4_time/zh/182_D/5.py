def solve():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    b = 0
    for i in range(n):
        b += a[i]
        ans = max(ans,b)
    print(ans)
solve()
