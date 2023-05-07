def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(0)
        return
    if N == 2:
        if XY[0] == XY[1]:
            print(1)
            print(1)
            print('R')
            print('L')
        else:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        return
    # N >= 3
    if len(set(XY)) == 1:
        print(1)
        print(1)
        print('R' * (N - 1))
        print('L' * (N - 1))
        return
    if len(set(XY[0])) == 1:
        print(2)
        print(1, 1)
        print('R' * (N - 1))
        print('L' * (N - 1))
        return
    if len(set(XY[1])) == 1:
        print(2)
        print(1, 1)
        print('U' * (N - 1))
        print('D' * (N - 1))
        return
    # N >= 3
    if len(set(XY[0][0] + XY[1][0] + XY[2][0])) == 1:
        print(3)
        print(1, 1, 1)
        print('R' * (N - 1))
        print('L' * (N - 1))
        print('R' * (N - 1))
        return
    if len(set(XY[0][1] + XY[1][1] + XY[2][1])) == 1:
        print(3)
        print(1, 1, 1)
        print('U' * (N - 1))
        print('D' * (N - 1))
        print('U' * (N - 1))
        return
    # N >= 3
    if len(set(XY[0][0] + XY[1][0] + XY[2][0] + XY[3][0])) == 1:
        print(4)
        print(1, 1,
