def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(0)
        return
    if N == 2:
        if XY[0] != XY[1]:
            print(-1)
        else:
            print(1)
            print(1, 1)
            print('RU')
            print('UR')
        return
    if N == 3:
        if XY[0] == XY[1] == XY[2]:
            print(1)
            print(1, 1)
            print('RU')
            print('UR')
            return
        if XY[0] == XY[1] or XY[1] == XY[2] or XY[2] == XY[0]:
            print(-1)
            return
        if XY[0][0] == XY[1][0] == XY[2][0] or XY[0][1] == XY[1][1] == XY[2][1]:
            print(-1)
            return
        if XY[0][0] == XY[1][0] and XY[1][0] != XY[2][0]:
            print(4)
            print(1, 1, 1, 1)
            print('R' * (XY[2][0] - XY[0][0]))
            print('U' * (XY[2][1] - XY[0][1]))
            print('R' * (XY[1][0] - XY[0][0]))
            print('U' * (XY[1][1] - XY[0][1]))
            return
        if XY[1][0] == XY[2][0] and XY[2][0] != XY[0][0]:
            print(4)
            print(1, 1, 1, 1)
            print('R' * (XY[1][0] - XY[0][0]))
            print('U' * (XY[1][1] - XY[0][1]))
            print('R' * (XY[2][0] - XY[1][0]))
            print('U' * (XY[2][1] - XY[1][1]))
            return
        if XY[2][
