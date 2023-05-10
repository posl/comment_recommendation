def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    if n == 1:
        print(0)
        print(0)
        print('')
    elif n == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        if x0 == x1:
            print(1)
            print(abs(y0 - y1))
            if y0 > y1:
                print('D')
            else:
                print('U')
        elif y0 == y1:
            print(1)
            print(abs(x0 - x1))
            if x0 > x1:
                print('L')
            else:
                print('R')
        else:
            print(-1)
    else:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        if x0 == x1 == x2:
            print(1)
            print(abs(y0 - y1))
            if y0 > y1:
                print('D')
            else:
                print('U')
        elif y0 == y1 == y2:
            print(1)
            print(abs(x0 - x1))
            if x0 > x1:
                print('L')
            else:
                print('R')
        else:
            print(3)
            print(abs(x0 - x1) + abs(x1 - x2))
            if x0 > x1:
                print('L' * abs(x0 - x1), end='')
            else:
                print('R' * abs(x0 - x1), end='')
            if x1 > x2:
                print('L' * abs(x1 - x2), end='')
            else:
                print('R' * abs(x1 - x2), end='')
            print()
            if y0 > y1:
                print('D' * abs(y0 - y1), end='')
            else:
                print('U' * abs(y0 - y1), end='')
            if y1 > y2:
                print('D' * abs(y1 - y2), end='')
            else:
                print('U' * abs(y1 - y2
