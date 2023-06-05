def solve():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    ab.sort(key=lambda x: x[1])
    cur = 1
    for a, b in ab:
        if a <= cur <= b:
            cur = b
    print(cur)
