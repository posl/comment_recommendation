def main():
    bingo = [[int(i) for i in input().split()] for i in range(3)]
    N = int(input())
    B = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in B:
                bingo[i][j] = 0
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0 or bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print('Yes')
        return
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0 or bingo[0][i] == bingo[1][i] == bingo[2][i] == 0:
            print('Yes')
            return
    print('No')
