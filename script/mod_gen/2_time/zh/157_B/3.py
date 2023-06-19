def bingo():
    bingo_list = []
    for i in range(3):
        bingo_list.append(list(map(int, input().split())))
    n = int(input())
    b_list = []
    for i in range(n):
        b_list.append(int(input()))
    for i in range(3):
        for j in range(3):
            if bingo_list[i][j] in b_list:
                bingo_list[i][j] = 0
    for i in range(3):
        if sum(bingo_list[i]) == 0:
            return True
    for i in range(3):
        if bingo_list[0][i] + bingo_list[1][i] + bingo_list[2][i] == 0:
            return True
    if bingo_list[0][0] + bingo_list[1][1] + bingo_list[2][2] == 0:
        return True
    if bingo_list[0][2] + bingo_list[1][1] + bingo_list[2][0] == 0:
        return True
    return False

if __name__ == '__main__':
    bingo()