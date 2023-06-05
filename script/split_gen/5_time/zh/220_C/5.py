def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = sum(a)
    ans = (x // s) * n
    x %= s
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        ans += 1
    print(ans)
solve()
