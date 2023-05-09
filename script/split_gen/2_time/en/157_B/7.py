def main():
    N = int(input())
    b = [int(input()) for _ in range(N)]
    bingo = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                bingo[i][j] = 1
    for i in range(3):
        if bingo[i][0] == 1 and bingo[i][1] == 1 and bingo[i][2] == 1:
            print('Yes')
            return
        if bingo[0][i] == 1 and bingo[1][i] == 1 and bingo[2][i] == 1:
            print('Yes')
            return
    if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1:
        print('Yes')
        return
    if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1:
        print('Yes')
        return
    print('No')
