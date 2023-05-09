def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(2)
        print(1, 1)
        print('RU')
        print('UR')
        return
    if N == 2:
        if sum(XY[0]) == sum(XY[1]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return
    if N == 3:
        if sum(XY[0]) == sum(XY[1]) == sum(XY[2]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return
    if N == 4:
        if sum(XY[0]) == sum(XY[1]) == sum(XY[2]) == sum(XY[3]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return
    if N == 5:
        if sum(XY[0]) == sum(XY[1]) == sum(XY[2]) == sum(XY[3]) == sum(XY[4]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return
    print(-1)
