def main():
    card = []
    for i in range(3):
        card.append(list(map(int, input().split())))
    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if card[j][k] == b:
                    card[j][k] = 0
    bingo = 0
    for i in range(3):
        if card[i][0] == card[i][1] == card[i][2] == 0:
            bingo = 1
        if card[0][i] == card[1][i] == card[2][i] == 0:
            bingo = 1
    if card[0][0] == card[1][1] == card[2][2] == 0:
        bingo = 1
    if card[0][2] == card[1][1] == card[2][0] == 0:
        bingo = 1
    if bingo == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()