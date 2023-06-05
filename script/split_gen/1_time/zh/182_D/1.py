def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]
        if i % 2 == 1:
            ans -= 2 * a[i]
    print(ans)
