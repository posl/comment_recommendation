def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        return 0, []
    if N == 2:
        x0, y0 = XY[0]
        x1, y1 = XY[1]
        if x0 == x1:
            return 1, [abs(y1-y0)], ['U' if y1 > y0 else 'D']
        elif y0 == y1:
            return 1, [abs(x1-x0)], ['R' if x1 > x0 else 'L']
        else:
            return 2, [abs(x1-x0), abs(y1-y0)], ['RU' if x1 > x0 else 'LU', 'RD' if x1 > x0 else 'LD']
    if N == 3:
        x0, y0 = XY[0]
        x1, y1 = XY[1]
        x2, y2 = XY[2]
        if x0 == x1 and x1 == x2:
            return 1, [abs(y2-y0)], ['U' if y2 > y0 else 'D']
        elif y0 == y1 and y1 == y2:
            return 1, [abs(x2-x0)], ['R' if x2 > x0 else 'L']
        else:
            return 2, [abs(x2-x0), abs(y2-y0)], ['RU' if x2 > x0 else 'LU', 'RD' if x2 > x0 else 'LD']
    if N == 4:
        x0, y0 = XY[0]
        x1, y1 = XY[1]
        x2, y2 = XY[2]
        x3, y3 = XY[3]
        if x0 == x1 and x1 == x2 and x2 == x3:
            return 1, [abs(y3-y0)], ['U' if y3 > y0 else 'D']
        elif y0 == y1 and y1 == y2 and y2 == y3:
            return 1, [abs(x3-x0)], ['R' if x3 > x0 else 'L']
        else:
            return 2, [abs(x3-x
