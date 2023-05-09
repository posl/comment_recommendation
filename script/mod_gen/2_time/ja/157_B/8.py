def main():
    bingo_card = []
    for i in range(3):
        bingo_card.append(list(map(int,input().split())))
    N = int(input())
    b = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            if bingo_card[i][j] in b:
                bingo_card[i][j] = 0
    for i in range(3):
        if bingo_card[i][0] == 0 and bingo_card[i][1] == 0 and bingo_card[i][2] == 0:
            print("Yes")
            return
    for i in range(3):
        if bingo_card[0][i] == 0 and bingo_card[1][i] == 0 and bingo_card[2][i] == 0:
            print("Yes")
            return
    if bingo_card[0][0] == 0 and bingo_card[1][1] == 0 and bingo_card[2][2] == 0:
        print("Yes")
        return
    if bingo_card[0][2] == 0 and bingo_card[1][1] == 0 and bingo_card[2][0] == 0:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()