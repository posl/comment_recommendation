def main():
    card = []
    for i in range(3):
        card.append(list(map(int, input().split())))
    n = int(input())
    bingo = []
    for i in range(n):
        bingo.append(int(input()))
    for i in range(3):
        for j in range(3):
            if card[i][j] in bingo:
                card[i][j] = 0
    if card[0][0] == 0 and card[0][1] == 0 and card[0][2] == 0 or card[1][0] == 0 and card[1][1] == 0 and card[1][2] == 0 or card[2][0] == 0 and card[2][1] == 0 and card[2][2] == 0 or card[0][0] == 0 and card[1][0] == 0 and card[2][0] == 0 or card[0][1] == 0 and card[1][1] == 0 and card[2][1] == 0 or card[0][2] == 0 and card[1][2] == 0 and card[2][2] == 0 or card[0][0] == 0 and card[1][1] == 0 and card[2][2] == 0 or card[0][2] == 0 and card[1][1] == 0 and card[2][0] == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()