def solve():
    import sys
    import math
    input = sys.stdin.readline
    a, b = map(int, input().split())
    c = 0
    while True:
        if a * c >= b:
            break
        c += 1
    g = 1
    ans = 0
    while True:
        ans += a / math.sqrt(g)
        if g == c + 1:
            break
        g += 1
    print(ans)

if __name__ == '__main__':
    solve()