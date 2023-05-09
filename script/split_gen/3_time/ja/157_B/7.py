def main():
    bingo = [list(map(int, input().split())) for i in range(3)]
    N = int(input())
    b = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = 0
    #print(bingo)
    if bingo[0][0] == bingo[0][1] == bingo[0][2] == 0 or bingo[1][0] == bingo[1][1] == bingo[1][2] == 0 or bingo[2][0] == bingo[2][1] == bingo[2][2] == 0 or bingo[0][0] == bingo[1][0] == bingo[2][0] == 0 or bingo[0][1] == bingo[1][1] == bingo[2][1] == 0 or bingo[0][2] == bingo[1][2] == bingo[2][2] == 0 or bingo[0][0] == bingo[1][1] == bingo[2][2] == 0 or bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print("Yes")
    else:
        print("No")
