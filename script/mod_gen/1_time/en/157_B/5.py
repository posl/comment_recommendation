def bingo():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    n = int(input())
    for i in range(n):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo[j][k] == b:
                    bingo[j][k] = 0
    for i in range(3):
        if bingo[i] == [0, 0, 0]:
            print("Yes")
            return
    for i in range(3):
        if bingo[0][i] == 0 and bingo[1][i] == 0 and bingo[2][i] == 0:
            print("Yes")
            return
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[0][2] == 0 and bingo[1][1] == 0 and bingo[2][0] == 0:
        print("Yes")
        return
    print("No")
bingo()

if __name__ == '__main__':
    bingo()