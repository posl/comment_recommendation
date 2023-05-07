def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(0)
        return
    if N == 2:
        if XY[0][0] == XY[1][0] and XY[0][1] == XY[1][1]:
            print(1)
            print(1)
            print('R')
            print('L')
            return
        else:
            print(-1)
            return
    if N == 3:
        if XY[0][0] == XY[1][0] and XY[0][1] == XY[1][1]:
            if XY[1][0] == XY[2][0] and XY[1][1] == XY[2][1]:
                print(2)
                print(1, 1)
                print('RU')
                print('UR')
                return
            else:
                print(-1)
                return
        else:
            print(-1)
            return
    if N == 4:
        if XY[0][0] == XY[1][0] and XY[0][1] == XY[1][1]:
            if XY[1][0] == XY[2][0] and XY[1][1] == XY[2][1]:
                if XY[2][0] == XY[3][0] and XY[2][1] == XY[3][1]:
                    print(3)
                    print(1, 1, 1)
                    print('RRU')
                    print('URR')
                    print('RUR')
                    return
                else:
                    print(-1)
                    return
            else:
                print(-1)
                return
        else:
            print(-1)
            return
    if N == 5:
        if XY[0][0] == XY[1][0] and XY[0][1] == XY[1][1]:
            if XY[1][0] == XY[2][0] and XY[1][1] == XY[2][1]:
                if XY[2][0] == XY[3][0] and XY[2][1] == XY[3][1]:
                    if XY[3][0] == XY[4][0] and XY[

if __name__ == '__main__':
    main()