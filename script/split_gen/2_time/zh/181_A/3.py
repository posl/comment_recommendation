def solve():
    x, y, a, b = map(int, input().split())
    ans = 0
    while x < y and x < (y - b) // a:
        x *= a
        ans += 1
    ans += (y - 1 - x) // b
    print(ans)
