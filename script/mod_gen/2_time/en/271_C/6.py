def solve():
    N = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 1
    for i in range(N):
        if ans >= 10**18:
            ans = 0
            break
        ans *= a[i]
        if ans > 10**18:
            ans = 0
            break
    print(ans)
solve()
