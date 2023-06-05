def solve():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 10**9
    for b in range(-100,101):
        tmp = 0
        for i in range(n):
            tmp += abs(a[i]-(b+i+1))
        ans = min(ans,tmp)
    print(ans)
solve()
