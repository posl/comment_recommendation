def main():
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
        for _ in range(l):
            if d == 'L':
                c_s -= 1
            elif d == 'R':
                c_s += 1
            elif d == 'U':
                r_s -= 1
            elif d == 'D':
                r_s += 1
            if (r_s, c_s) in walls:
                if d == 'L':
                    c_s += 1
                elif d == 'R':
                    c_s -= 1
                elif d == 'U':
                    r_s += 1
                elif d == 'D':
                    r_s -= 1
        print(r_s, c_s)
