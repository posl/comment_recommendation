def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(a[i]-i, 0)
    print(ans)
solve()
