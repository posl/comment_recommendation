def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(0)
        return
    if N == 2:
        if XY[0] == XY[1]:
            print(1)
            print(1)
            print('R')
            return
        else:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
    if N == 3:
        if XY[0] == XY[1] == XY[2]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        elif XY[0] == XY[1] or XY[1] == XY[2] or XY[2] == XY[0]:
            print(3)
            print(1, 1, 1)
            print('RUU')
            print('URU')
            print('UUR')
            return
        else:
            print(4)
            print(1, 1, 1, 1)
            print('RUUR')
            print('URUR')
            print('UURU')
            print('URUR')
            return
    if N == 4:
        if XY[0] == XY[1] == XY[2] == XY[3]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        elif XY[0] == XY[1] == XY[2] or XY[0] == XY[1] == XY[3] or XY[0] == XY[2] == XY[3] or XY[1] == XY[2] == XY[3]:
            print(5)
            print(1, 1, 1, 1, 1)
            print('RUURU')
            print('URURU')
            print('UURUR')
            print('URURU')
            print('RUURU')
            return
        else:
            print(6)
            print(1, 1, 1, 1, 1, 1)
            print('RUURUR')
            print('URURUR')
            print('UURURU')
            print

if __name__ == '__main__':
    main()