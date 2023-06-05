def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    now = 0
    for i in range(n - 1):
        now += a[i]
        ans = min(ans, abs(s - 2 * now))
    print(ans)
