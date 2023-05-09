def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for _ in range(N):
        r, c = map(int, input().split())
        wall.add((r, c))
    Q = int(input())
    d = {d: (dr, dc) for d, (dr, dc) in zip('LRUD', ((0, -1), (0, 1), (-1, 0), (1, 0)))}
    for _ in range(Q):
        di, l = input().split()
        dr, dc = d[di]
        l = int(l)
        for i in range(l):
            r_s += dr
            c_s += dc
            if (r_s, c_s) in wall:
                r_s -= dr
                c_s -= dc
                break
        print(r_s, c_s)
