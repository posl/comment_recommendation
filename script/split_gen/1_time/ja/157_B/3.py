def bingo():
    bingo_card = []
    for i in range(3):
        bingo_card.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            for k in range(n):
                if bingo_card[i][j] == b[k]:
                    bingo_card[i][j] = 0
    for i in range(3):
        if bingo_card[i][0] == bingo_card[i][1] == bingo_card[i][2] == 0:
            return True
        if bingo_card[0][i] == bingo_card[1][i] == bingo_card[2][i] == 0:
            return True
    if bingo_card[0][0] == bingo_card[1][1] == bingo_card[2][2] == 0:
        return True
    if bingo_card[0][2] == bingo_card[1][1] == bingo_card[2][0] == 0:
        return True
    return False
