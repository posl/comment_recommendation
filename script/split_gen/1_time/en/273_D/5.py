def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for i in range(l):
                c_s -= 1
                if (r_s, c_s) in walls:
                    c_s += 1
                    break
        elif d == 'R':
            for i in range(l):
                c_s += 1
                if (r_s, c_s) in walls:
                    c_s -= 1
                    break
        elif d == 'U':
            for i in range(l):
                r_s -= 1
                if (r_s, c_s) in walls:
                    r_s += 1
                    break
        elif d == 'D':
            for i in range(l):
                r_s += 1
                if (r_s, c_s) in walls:
                    r_s -= 1
                    break
        print(r_s, c_s)
solve()
