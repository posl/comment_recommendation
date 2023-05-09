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
        d = max(abs(XY[0][0] - XY[1][0]), abs(XY[0][1] - XY[1][1]))
        print(2)
        print(d, d)
        print('RU')
        print('UR')
        return
    d = max(abs(XY[0][0] - XY[1][0]), abs(XY[0][1] - XY[1][1]))
    for i in range(2, N):
        d = max(d, abs(XY[0][0] - XY[i][0]), abs(XY[0][1] - XY[i][1]))
    print(2)
    print(d, d)
    print('RU')
    print('UR')
