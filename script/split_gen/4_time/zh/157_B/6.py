def bingo():
    bingo_map = []
    for i in range(3):
        bingo_map.append(list(map(int, input().split())))
    bingo_num = int(input())
    bingo_list = []
    for i in range(bingo_num):
        bingo_list.append(int(input()))
    for i in range(3):
        for j in range(3):
            if bingo_map[i][j] in bingo_list:
                bingo_map[i][j] = 0
    #print(bingo_map)
    if bingo_map[0][0] == bingo_map[0][1] == bingo_map[0][2] == 0:
        print('Yes')
        return
    if bingo_map[1][0] == bingo_map[1][1] == bingo_map[1][2] == 0:
        print('Yes')
        return
    if bingo_map[2][0] == bingo_map[2][1] == bingo_map[2][2] == 0:
        print('Yes')
        return
    if bingo_map[0][0] == bingo_map[1][0] == bingo_map[2][0] == 0:
        print('Yes')
        return
    if bingo_map[0][1] == bingo_map[1][1] == bingo_map[2][1] == 0:
        print('Yes')
        return
    if bingo_map[0][2] == bingo_map[1][2] == bingo_map[2][2] == 0:
        print('Yes')
        return
    if bingo_map[0][0] == bingo_map[1][1] == bingo_map[2][2] == 0:
        print('Yes')
        return
    if bingo_map[0][2] == bingo_map[1][1] == bingo_map[2][0] == 0:
        print('Yes')
        return
    print('No')
    return
bingo()
