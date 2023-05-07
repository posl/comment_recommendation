def main():
    # ビンゴカードの作成
    card = []
    for i in range(3):
        card.append(list(map(int, input().split())))
    #print(card)
    # カードに印をつける
    n = int(input())
    for i in range(n):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if card[j][k] == b:
                    card[j][k] = 0
    #print(card)
    # ビンゴの判定
    # 横
    for i in range(3):
        if card[i][0] == 0 and card[i][1] == 0 and card[i][2] == 0:
            print("Yes")
            exit()
    # 縦
    for i in range(3):
        if card[0][i] == 0 and card[1][i] == 0 and card[2][i] == 0:
            print("Yes")
            exit()
    # 斜め
    if card[0][0] == 0 and card[1][1] == 0 and card[2][2] == 0:
        print("Yes")
        exit()
    if card[0][2] == 0 and card[1][1] == 0 and card[2][0] == 0:
        print("Yes")
        exit()
    print("No")

if __name__ == '__main__':
    main()