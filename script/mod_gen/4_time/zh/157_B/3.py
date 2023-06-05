def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo[j][k] == b:
                    bingo[j][k] = 0
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0:
            print("Yes")
            exit()
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == 0:
            print("Yes")
            exit()
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
        print("Yes")
        exit()
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print("Yes")
        exit()
    print("No")

if __name__ == '__main__':
    main()