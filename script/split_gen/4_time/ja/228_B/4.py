def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    ans = 1
    while x != a[x]:
        x = a[x]
        ans += 1
        if ans > n:
            ans = -1
            break
    print(ans)
