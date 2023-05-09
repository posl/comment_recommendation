def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(1)
        print(1)
        print('R')
        return
    if N == 2:
        if XY[0] == XY[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        else:
            print(-1)
            return
    if N == 3:
        if XY[0] == XY[1] == XY[2]:
            print(3)
            print(1, 1, 1)
            print('RUU')
            print('URU')
            print('UUR')
            return
        else:
            print(-1)
            return
    if N == 4:
        if XY[0] == XY[1] == XY[2] == XY[3]:
            print(4)
            print(1, 1, 1, 1)
            print('RUUU')
            print('URUU')
            print('UURU')
            print('UUUR')
            return
        else:
            print(-1)
            return
    if N == 5:
        if XY[0] == XY[1] == XY[2] == XY[3] == XY[4]:
            print(5)
            print(1, 1, 1, 1, 1)
            print('RUUUU')
            print('URUUU')
            print('UURUU')
            print('UUURU')
            print('UUUUR')
            return
        else:
            print(-1)
            return
    if N == 6:
        if XY[0] == XY[1] == XY[2] == XY[3] == XY[4] == XY[5]:
            print(6)
            print(1, 1, 1, 1, 1, 1)
            print('RUUUUU')
            print('URUUUU')
            print('UURUUU')
            print('UUURUU')
            print('UUUURU')
            print('UUUUUR')
            return
        else:
            print(-1)
            return
    if N == 7:
        if XY[0
