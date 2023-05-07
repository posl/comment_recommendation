def bingo():
    bingo_card = []
    for i in range(3):
        bingo_card.append(list(map(int, input().split())))
    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo_card[j][k] == b:
                    bingo_card[j][k] = 0
    if bingo_card[0][0] == bingo_card[0][1] == bingo_card[0][2] == 0:
        print("Yes")
    elif bingo_card[1][0] == bingo_card[1][1] == bingo_card[1][2] == 0:
        print("Yes")
    elif bingo_card[2][0] == bingo_card[2][1] == bingo_card[2][2] == 0:
        print("Yes")
    elif bingo_card[0][0] == bingo_card[1][0] == bingo_card[2][0] == 0:
        print("Yes")
    elif bingo_card[0][1] == bingo_card[1][1] == bingo_card[2][1] == 0:
        print("Yes")
    elif bingo_card[0][2] == bingo_card[1][2] == bingo_card[2][2] == 0:
        print("Yes")
    elif bingo_card[0][0] == bingo_card[1][1] == bingo_card[2][2] == 0:
        print("Yes")
    elif bingo_card[0][2] == bingo_card[1][1] == bingo_card[2][0] == 0:
        print("Yes")
    else:
        print("No")
