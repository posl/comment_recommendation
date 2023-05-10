def check_bingo(bingo_list):
    is_bingo = False
    for i in range(3):
        if bingo_list[i][0] == bingo_list[i][1] == bingo_list[i][2] == 1:
            is_bingo = True
        if bingo_list[0][i] == bingo_list[1][i] == bingo_list[2][i] == 1:
            is_bingo = True
    if bingo_list[0][0] == bingo_list[1][1] == bingo_list[2][2] == 1:
        is_bingo = True
    if bingo_list[0][2] == bingo_list[1][1] == bingo_list[2][0] == 1:
        is_bingo = True
    return is_bingo
bingo_list = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    bingo_list[i] = list(map(int, input().split()))
N = int(input())
b_list = [0 for i in range(N)]
for i in range(N):
    b_list[i] = int(input())
for i in range(N):
    for j in range(3):
        for k in range(3):
            if b_list[i] == bingo_list[j][k]:
                bingo_list[j][k] = 1

if __name__ == '__main__':
    check_bingo()