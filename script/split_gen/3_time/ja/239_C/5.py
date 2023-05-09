def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x1 - x2
    dy = y1 - y2
    dx, dy = abs(dx), abs(dy)
    if dx == 0 and dy == 0:
        print('No')
    elif dx == dy:
        print('Yes')
    elif dx == 0 or dy == 0:
        print('Yes')
    elif dx % 2 == 0 and dy % 2 == 0:
        print('Yes')
    elif dx % 2 == 1 and dy % 2 == 1:
        print('Yes')
    else:
        print('No')
