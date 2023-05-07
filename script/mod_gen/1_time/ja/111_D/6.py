def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    if N == 1:
        if XY[0] == (0, 0):
            print(0)
        else:
            print(1)
            print(1)
            print('R' if XY[0][0] > 0 else 'L')
            print('U' if XY[0][1] > 0 else 'D')
        return
    XY.sort()
    XY = [(0, 0)] + XY
    # まずは、各軸について、全点を通るようなパスが存在するかをチェック
    for i in range(1, N + 1):
        if abs(XY[i][0] - XY[i - 1][0]) % 2 == 1 or abs(XY[i][1] - XY[i - 1][1]) % 2 == 1:
            print(-1)
            return
    # あとは、各軸について、全点を通るようなパスを作る
    ans = []
    for i in range(1, N + 1):
        x = XY[i][0]
        y = XY[i][1]
        ans.append('R' * (x - XY[i - 1][0]) + 'U' * (y - XY[i - 1][1]))
    print(N * 2)
    print(' '.join(['1'] * N * 2))
    print('
'.join(ans))

if __name__ == '__main__':
    main()