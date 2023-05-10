def solve():
    #import sys
    #input = sys.stdin.readline
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    right = -1
    for a, b in ab:
        if a > right:
            ans += 1
            right = b - 1
    print(ans)
    return 0
