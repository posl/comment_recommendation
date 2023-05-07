def bingo_check(bingo, b):
    for i in range(3):
        if(bingo[i][0] == b and bingo[i][1] == b and bingo[i][2] == b):
            return True
        if(bingo[0][i] == b and bingo[1][i] == b and bingo[2][i] == b):
            return True
    if(bingo[0][0] == b and bingo[1][1] == b and bingo[2][2] == b):
        return True
    if(bingo[0][2] == b and bingo[1][1] == b and bingo[2][0] == b):
        return True
    return False
bingo = list()
for i in range(3):
    bingo.append(list(map(int, input().split())))
n = int(input())
b = list()
for i in range(n):
    b.append(int(input()))
for i in range(n):
    for j in range(3):
        for k in range(3):
            if(bingo[j][k] == b[i]):
                bingo[j][k] = 0
for i in range(n):
    if(bingo_check(bingo, 0)):
        print("Yes")
        exit()
print("No")

if __name__ == '__main__':
    bingo_check()