def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    a = [x[0] for x in ab]
    b = [x[1] for x in ab]
    a.sort()
    b.sort()
    print(max(a[-1], b[-1]))
