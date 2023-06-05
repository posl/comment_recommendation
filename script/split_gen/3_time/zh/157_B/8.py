def main():
    bingo = [[], [], []]
    for i in range(3):
        bingo[i] = list(map(int, input().split()))
    n = int(input())
    b = [0] * n
    for i in range(n):
        b[i] = int(input())
    for i in range(3):
        for j in range(3):
            for k in range(n):
                if bingo[i][j] == b[k]:
                    bingo[i][j] = 0
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0:
            print("Yes")
            return
    for i in range(3):
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == 0:
            print("Yes")
            return
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print("Yes")
        return
    print("No")
