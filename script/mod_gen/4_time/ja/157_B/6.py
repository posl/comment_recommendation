def check_bingo(bingo):
    #縦
    for i in range(3):
        if bingo[0][i] == bingo[1][i] == bingo[2][i]:
            return True
    #横
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2]:
            return True
    #斜め
    if bingo[0][0] == bingo[1][1] == bingo[2][2]:
        return True
    if bingo[0][2] == bingo[1][1] == bingo[2][0]:
        return True
    return False

if __name__ == '__main__':
    check_bingo()