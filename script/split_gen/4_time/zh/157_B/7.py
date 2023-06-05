def bingo(bingo_card, bingo_num):
    bingo_line = [[bingo_card[0][0], bingo_card[0][1], bingo_card[0][2]],
                  [bingo_card[1][0], bingo_card[1][1], bingo_card[1][2]],
                  [bingo_card[2][0], bingo_card[2][1], bingo_card[2][2]],
                  [bingo_card[0][0], bingo_card[1][0], bingo_card[2][0]],
                  [bingo_card[0][1], bingo_card[1][1], bingo_card[2][1]],
                  [bingo_card[0][2], bingo_card[1][2], bingo_card[2][2]],
                  [bingo_card[0][0], bingo_card[1][1], bingo_card[2][2]],
                  [bingo_card[0][2], bingo_card[1][1], bingo_card[2][0]]]
    for i in range(len(bingo_line)):
        if set(bingo_line[i]) & set(bingo_num) == set(bingo_line[i]):
            return 'Yes'
    return 'No'
