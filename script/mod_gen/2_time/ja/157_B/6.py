def main():
    bingo = []
    for _ in range(3):
        bingo.append(list(map(int, input().split())))
    n = int(input())
    b = [int(input()) for _ in range(n)]
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = 0
    if bingo[0][0] == 0 and bingo[0][1] == 0 and bingo[0][2] == 0:
        print("Yes")
        return
    if bingo[1][0] == 0 and bingo[1][1] == 0 and bingo[1][2] == 0:
        print("Yes")
        return
    if bingo[2][0] == 0 and bingo[2][1] == 0 and bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[0][0] == 0 and bingo[1][0] == 0 and bingo[2][0] == 0:
        print("Yes")
        return
    if bingo[0][1] == 0 and bingo[1][1] == 0 and bingo[2][1] == 0:
        print("Yes")
        return
    if bingo[0][2] == 0 and bingo[1][2] == 0 and bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0:
        print("Yes")
        return
    if bingo[0][2] == 0 and bingo[1][1] == 0 and bingo[2][0] == 0:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()