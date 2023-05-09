def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = 0
    for i in range(3):
        if bingo[i][0] == 0 and bingo[i][1] == 0 and bingo[i][2] == 0:
            print("Yes")
            return
        if bingo[0][i] == 0 and bingo[1][i] == 0 and bingo[2][i] == 0:
            print("Yes")
            return
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[2][0] == 0 and bingo[1][1] == 0 and bingo[0][2] == 0:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()