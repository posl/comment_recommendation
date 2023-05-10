def main():
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append(list(map(int, input().split())))
    if N == 1:
        print(1)
        print(1)
        print('U')
        return
    if N == 2:
        if XY[0][0] == XY[1][0] or XY[0][1] == XY[1][1]:
            print(1)
            print(1)
            print('U')
        else:
            print(2)
            print(1, 1)
            print('LR')
        return
    if N == 3:
        if XY[0][0] == XY[1][0] and XY[1][0] == XY[2][0]:
            print(2)
            print(1, 1)
            print('LR')
        elif XY[0][1] == XY[1][1] and XY[1][1] == XY[2][1]:
            print(2)
            print(1, 1)
            print('UD')
        else:
            print(3)
            print(1, 1, 1)
            print('LUR')
        return

if __name__ == '__main__':
    main()