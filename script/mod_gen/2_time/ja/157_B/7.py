def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int,input().split())))
    N = int(input())
    b = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = "OK"
    if bingo[0][0] == "OK" and bingo[0][1] == "OK" and bingo[0][2] == "OK":
        print("Yes")
        return
    if bingo[1][0] == "OK" and bingo[1][1] == "OK" and bingo[1][2] == "OK":
        print("Yes")
        return
    if bingo[2][0] == "OK" and bingo[2][1] == "OK" and bingo[2][2] == "OK":
        print("Yes")
        return
    if bingo[0][0] == "OK" and bingo[1][0] == "OK" and bingo[2][0] == "OK":
        print("Yes")
        return
    if bingo[0][1] == "OK" and bingo[1][1] == "OK" and bingo[2][1] == "OK":
        print("Yes")
        return
    if bingo[0][2] == "OK" and bingo[1][2] == "OK" and bingo[2][2] == "OK":
        print("Yes")
        return
    if bingo[0][0] == "OK" and bingo[1][1] == "OK" and bingo[2][2] == "OK":
        print("Yes")
        return
    if bingo[0][2] == "OK" and bingo[1][1] == "OK" and bingo[2][0] == "OK":
        print("Yes")
        return
    print("No")
    return

if __name__ == '__main__':
    main()