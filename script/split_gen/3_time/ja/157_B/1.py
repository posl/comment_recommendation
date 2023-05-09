def main():
    bingo = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    b = [int(input()) for _ in range(N)]
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = 0
    for i in range(3):
        if bingo[i] == [0, 0, 0]:
            print("Yes")
            return
    for j in range(3):
        if bingo[0][j] == bingo[1][j] == bingo[2][j] == 0:
            print("Yes")
            return
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print("Yes")
        return
    print("No")
