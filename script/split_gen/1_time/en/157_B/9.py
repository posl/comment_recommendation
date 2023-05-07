def bingo_check(bingo_card, bingo_num):
    #check horizontal
    for i in range(3):
        if bingo_card[i][0] in bingo_num and bingo_card[i][1] in bingo_num and bingo_card[i][2] in bingo_num:
            return True
    #check vertical
    for j in range(3):
        if bingo_card[0][j] in bingo_num and bingo_card[1][j] in bingo_num and bingo_card[2][j] in bingo_num:
            return True
    #check diagonal
    if bingo_card[0][0] in bingo_num and bingo_card[1][1] in bingo_num and bingo_card[2][2] in bingo_num:
        return True
    if bingo_card[0][2] in bingo_num and bingo_card[1][1] in bingo_num and bingo_card[2][0] in bingo_num:
        return True
    return False
