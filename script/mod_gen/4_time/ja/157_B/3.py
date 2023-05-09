def main():
    # 標準入力の受け取り
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    # ビンゴカードの作成
    bingocard = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                bingocard[i][j] = 1
    # ビンゴ判定
    # 縦
    for i in range(3):
        if bingocard[0][i] == 1 and bingocard[1][i] == 1 and bingocard[2][i] == 1:
            print('Yes')
            exit()
    # 横
    for i in range(3):
        if bingocard[i][0] == 1 and bingocard[i][1] == 1 and bingocard[i][2] == 1:
            print('Yes')
            exit()
    # 斜め
    if bingocard[0][0] == 1 and bingocard[1][1] == 1 and bingocard[2][2] == 1:
        print('Yes')
        exit()
    if bingocard[0][2] == 1 and bingocard[1][1] == 1 and bingocard[2][0] == 1:
        print('Yes')
        exit()
    print('No')

if __name__ == '__main__':
    main()