def bingo():
    sheet = []
    for i in range(3):
        sheet.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if sheet[i][j] in b:
                sheet[i][j] = 0
    for i in range(3):
        if sheet[i][0] == 0 and sheet[i][1] == 0 and sheet[i][2] == 0:
            return 'Yes'
    for i in range(3):
        if sheet[0][i] == 0 and sheet[1][i] == 0 and sheet[2][i] == 0:
            return 'Yes'
    if sheet[0][0] == 0 and sheet[1][1] == 0 and sheet[2][2] == 0:
        return 'Yes'
    if sheet[0][2] == 0 and sheet[1][1] == 0 and sheet[2][0] == 0:
        return 'Yes'
    return 'No'
print(bingo())

if __name__ == '__main__':
    bingo()