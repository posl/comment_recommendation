def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    flag = False
    for i in range(3):
        if bingo[i][0] in b and bingo[i][1] in b and bingo[i][2] in b:
            flag = True
    for i in range(3):
        if bingo[0][i] in b and bingo[1][i] in b and bingo[2][i] in b:
            flag = True
    if bingo[0][0] in b and bingo[1][1] in b and bingo[2][2] in b:
        flag = True
    if bingo[0][2] in b and bingo[1][1] in b and bingo[2][0] in b:
        flag = True
    if flag:
        print('Yes')
    else:
        print('No')
