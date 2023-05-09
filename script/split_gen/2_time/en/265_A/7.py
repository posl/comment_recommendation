def solve():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(n+1):
        ans = max(ans, (n-i)*x + i*y)
    print(ans)
