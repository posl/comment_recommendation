def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(0)
    elif N == 2:
        if XY[0][0] == XY[1][0] or XY[0][1] == XY[1][1]:
            print(1)
            print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]))
            print(''.join(['R' if XY[0][0] < XY[1][0] else 'L' if XY[0][0] > XY[1][0] else '',
                           'U' if XY[0][1] < XY[1][1] else 'D' if XY[0][1] > XY[1][1] else '']))
            print(''.join(['R' if XY[0][0] > XY[1][0] else 'L' if XY[0][0] < XY[1][0] else '',
                           'U' if XY[0][1] > XY[1][1] else 'D' if XY[0][1] < XY[1][1] else '']))
        else:
            print(2)
            print(abs(XY[0][0] - XY[1][0]), abs(XY[0][1] - XY[1][1]))
            print(''.join(['R' if XY[0][0] < XY[1][0] else 'L' if XY[0][0] > XY[1][0] else '',
                           'U' if XY[0][1] < XY[1][1] else 'D' if XY[0][1] > XY[1][1] else '']))
            print(''.join(['R' if XY[0][0] > XY[1][0] else 'L' if XY[0][0] < XY[1][0] else '',
                           'U' if XY[0][1] > XY[1][1] else 'D' if XY[0][1] < XY[1][1] else '']))
    else:
        if XY[0][0] == XY[1][0] or XY[0][1

if __name__ == '__main__':
    main()