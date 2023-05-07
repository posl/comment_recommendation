def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for a, b in ab:
        ans += a / b
    ans /= 2
    print(ans)
