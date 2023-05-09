def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    walls = set()
    for i in range(n):
        r, c = map(int, input().split())
        walls.add((r, c))
    q = int(input())
    instructions = []
    for i in range(q):
        d, l = input().split()
        instructions.append((d, int(l)))
    for d, l in instructions:
        for i in range(l):
            if d == 'L':
                cs -= 1
            elif d == 'R':
                cs += 1
            elif d == 'U':
                rs -= 1
            elif d == 'D':
                rs += 1
            if (rs, cs) in walls:
                if d == 'L':
                    cs += 1
                elif d == 'R':
                    cs -= 1
                elif d == 'U':
                    rs += 1
                elif d == 'D':
                    rs -= 1
                break
        print(rs, cs)
