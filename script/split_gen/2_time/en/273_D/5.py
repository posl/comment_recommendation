def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    ans = []
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for _ in range(l):
                if (r_s, c_s - 1) not in walls:
                    c_s -= 1
        elif d == 'R':
            for _ in range(l):
                if (r_s, c_s + 1) not in walls:
                    c_s += 1
        elif d == 'U':
            for _ in range(l):
                if (r_s - 1, c_s) not in walls:
                    r_s -= 1
        elif d == 'D':
            for _ in range(l):
                if (r_s + 1, c_s) not in walls:
                    r_s += 1
        ans.append((r_s, c_s))
    for r, c in ans:
        print(r, c)
