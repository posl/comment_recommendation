def bingo():
    bingo = []
    for i in range(3):
        bingo.append([int(x) for x in input().split()])
    N = int(input())
    b = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = 0
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0:
            return 'Yes'
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == 0:
            return 'Yes'
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
        return 'Yes'
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        return 'Yes'
    return 'No'
print(bingo())

if __name__ == '__main__':
    bingo()