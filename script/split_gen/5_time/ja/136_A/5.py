def solve():
    a, b, c = map(int, input().split())
    ans = max(0, c - (a - b))
    print(ans)
