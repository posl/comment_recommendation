def main():
    # H, W = map(int, input().split())
    # S = [list(input()) for _ in range(H)]
    H, W = 4, 6
    S = [
        ['#', '#', '.', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '#', '.'],
        ['#', '#', '.', '#', '.', '.']
    ]
    # まずは縦方向に照らされるマスを数える
    # その後、横方向に照らされるマスを数える
    # ちょっとややこしいので、縦方向のみを考える
    # そのために、縦方向の照らされるマスを数える関数を作る
    # その関数に、縦方向の照らされるマスを数える関数を渡す
    # 縦方向の照らされるマスを数える関数
    def count_light_v(S, H, W, x, y):
        count = 0
        # まずは上方向を数える
        for i in range(x, -1, -1):
            if S[i][y] == '#':
                break
            count += 1
        # 次に下方向を数える
        for i in range(x, H):
            if S[i][y] == '#':
                break
            count += 1
        return count
    # 横方向の照らされるマスを数える関数
    def count_light_h(S, H, W, x, y):
        count = 0
        # まずは左方向を数える
        for i in range(y, -1, -1):
            if S[x][i] == '#':
                break
            count += 1
        # 次に右方向を数える
        for i in range(y, W):
            if S[x][i] == '#':
                break
            count += 1
        return count

if __name__ == '__main__':
    main()