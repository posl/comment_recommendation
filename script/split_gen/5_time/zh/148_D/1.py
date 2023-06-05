def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            print(-1)
            return
    ans = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            ans += 1
        else:
            ans += a[i]
    print(ans)
solve()
