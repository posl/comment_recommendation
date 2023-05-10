def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    walls = []
    for i in range(N):
        r, c = map(int, input().split())
        walls.append((r, c))
    Q = int(input())
    query = []
    for i in range(Q):
        d, l = input().split()
        query.append((d, int(l)))
    wall_row = [0] * (H + 2)
    wall_col = [0] * (W + 2)
    for r, c in walls:
        wall_row[r] += 1
        wall_col[c] += 1
    row = rs
    col = cs
    for d, l in query:
        if d == 'L':
            for _ in range(l):
                col -= 1
                if wall_col[col] > 0:
                    col += 1
                    break
        elif d == 'R':
            for _ in range(l):
                col += 1
                if wall_col[col] > 0:
                    col -= 1
                    break
        elif d == 'U':
            for _ in range(l):
                row -= 1
                if wall_row[row] > 0:
                    row += 1
                    break
        elif d == 'D':
            for _ in range(l):
                row += 1
                if wall_row[row] > 0:
                    row -= 1
                    break
        else:
            assert False
    print(row, col)
