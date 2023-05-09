def main():
    #入力
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    #ビンゴカードの作成
    bingo_card = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                bingo_card[i][j] = 1
    #ビンゴの判定
    bingo = False
    #横
    for i in range(3):
        if sum(bingo_card[i]) == 3:
            bingo = True
    #縦
    for i in range(3):
        if sum([bingo_card[0][i], bingo_card[1][i], bingo_card[2][i]]) == 3:
            bingo = True
    #斜め
    if sum([bingo_card[0][0], bingo_card[1][1], bingo_card[2][2]]) == 3:
        bingo = True
    if sum([bingo_card[0][2], bingo_card[1][1], bingo_card[2][0]]) == 3:
        bingo = True
    #出力
    if bingo:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()