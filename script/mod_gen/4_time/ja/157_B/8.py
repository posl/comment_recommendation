def bingo_check(bingo_card, b):
    bingo = False
    for i in range(3):
        if bingo_card[i][0] in b and bingo_card[i][1] in b and bingo_card[i][2] in b:
            bingo = True
            break
        if bingo_card[0][i] in b and bingo_card[1][i] in b and bingo_card[2][i] in b:
            bingo = True
            break
    if bingo_card[0][0] in b and bingo_card[1][1] in b and bingo_card[2][2] in b:
        bingo = True
    if bingo_card[0][2] in b and bingo_card[1][1] in b and bingo_card[2][0] in b:
        bingo = True
    return bingo

if __name__ == '__main__':
    bingo_check()