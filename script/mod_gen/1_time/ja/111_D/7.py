def solve():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(1)
        print(1, 1)
        print('R')
        return
    if N == 2:
        if XY[0][0] == XY[1][0] or XY[0][1] == XY[1][1]:
            print(2)
            print(1, 1)
            print('RU' if XY[0][0] == XY[1][0] else 'UR')
            return
        else:
            print(3)
            print(1, 1, 1)
            print('RUR' if XY[0][0] < XY[1][0] else 'LUL')
            return
    print(3)
    print(1, 1, 1)
    print('RUR' if XY[0][0] < XY[1][0] else 'LUL')
    for i in range(1, N - 1):
        if XY[i][0] == XY[i + 1][0]:
            print('U' if XY[i][1] < XY[i + 1][1] else 'D')
        else:
            print('R' if XY[i][0] < XY[i + 1][0] else 'L')
solve()

if __name__ == '__main__':
    solve()