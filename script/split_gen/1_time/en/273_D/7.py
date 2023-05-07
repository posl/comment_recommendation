def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    walls = set()
    for _ in range(n):
        r, c = map(int, input().split())
        walls.add((r, c))
    q = int(input())
    for _ in range(q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for _ in range(l):
                cs -= 1
                if (rs, cs) in walls:
                    cs += 1
                    break
        elif d == 'R':
            for _ in range(l):
                cs += 1
                if (rs, cs) in walls:
                    cs -= 1
                    break
        elif d == 'U':
            for _ in range(l):
                rs -= 1
                if (rs, cs) in walls:
                    rs += 1
                    break
        elif d == 'D':
            for _ in range(l):
                rs += 1
                if (rs, cs) in walls:
                    rs -= 1
                    break
        print(rs, cs)
