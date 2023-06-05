def main():
    h, w, rs, cs = [int(x) for x in input().split()]
    n = int(input())
    rcs = [[int(x) for x in input().split()] for _ in range(n)]
    q = int(input())
    dls = [[x for x in input().split()] for _ in range(q)]
    walls = set()
    for rc in rcs:
        walls.add((rc[0], rc[1]))
    r, c = rs, cs
    for dl in dls:
        d, l = dl[0], int(dl[1])
        if d == 'L':
            for i in range(l):
                if (r, c - 1) not in walls:
                    c -= 1
        if d == 'R':
            for i in range(l):
                if (r, c + 1) not in walls:
                    c += 1
        if d == 'U':
            for i in range(l):
                if (r - 1, c) not in walls:
                    r -= 1
        if d == 'D':
            for i in range(l):
                if (r + 1, c) not in walls:
                    r += 1
        print(r, c)
