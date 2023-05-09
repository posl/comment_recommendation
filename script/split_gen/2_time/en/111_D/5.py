def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    if N == 1:
        print(0)
        exit()
    if N == 2:
        if XY[0][0] == XY[1][0] and XY[0][1] == XY[1][1]:
            print(1)
            print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]))
            print('R' * (XY[0][0] - XY[1][0]) + 'U' * (XY[0][1] - XY[1][1]))
            exit()
        else:
            print(2)
            print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]), 1)
            print('R' * (XY[0][0] - XY[1][0]) + 'U' * (XY[0][1] - XY[1][1]) + 'L')
            print('L' * (XY[0][0] - XY[1][0]) + 'D' * (XY[0][1] - XY[1][1]) + 'R')
            exit()
    else:
        print(3)
        print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]), abs(XY[0][0] - XY[2][0]) + abs(XY[0][1] - XY[2][1]), 1)
        print('R' * (XY[0][0] - XY[1][0]) + 'U' * (XY[0][1] - XY[1][1]) + 'L')
        print('R' * (XY[0][0] - XY[2][0]) + 'U' * (XY[0][1] - XY[2][1]) + 'L')
        print('L' * (XY[0][0] - XY[2][0]) + 'D' * (XY[0][1] - XY[2][1]) + 'R')
        exit
