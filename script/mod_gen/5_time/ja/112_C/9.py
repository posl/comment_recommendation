def main():
    # 1行目の入力を取得
    N = int(input())
    # 2行目以降の入力を取得
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    #print(data)
    # ピラミッドの中心座標と高さを特定する
    for i in range(N):
        if data[i][2] != 0:
            C_X = data[i][0]
            C_Y = data[i][1]
            H = data[i][2]
            break
    #print(C_X, C_Y, H)
    # ピラミッドの中心座標と高さを特定する
    for i in range(101):
        for j in range(101):
            #print(i, j)
            #print(data[0][2] + abs(data[0][0] - i) + abs(data[0][1] - j))
            #print(data[1][2] + abs(data[1][0] - i) + abs(data[1][1] - j))
            #print(data[2][2] + abs(data[2][0] - i) + abs(data[2][1] - j))
            #print(data[3][2] + abs(data[3][0] - i) + abs(data[3][1] - j))
            #print(data[4][2] + abs(data[4][0] - i) + abs(data[4][1] - j))
            for k in range(N):
                if data[k][2] != max(H - abs(data[k][0] - i) - abs(data[k][1] - j), 0):
                    break
            else:
                print(i, j, max(H - abs(data[k][0] - i) - abs(data[k][1] - j), 0))
                exit()

if __name__ == '__main__':
    main()