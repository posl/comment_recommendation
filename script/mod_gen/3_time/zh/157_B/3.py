def bingo():
    bingo = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3):
        for j in range(3):
            if bingo[0] == 1 and bingo[1] == 1 and bingo[2] == 1:
                return True
            if bingo[3] == 1 and bingo[4] == 1 and bingo[5] == 1:
                return True
            if bingo[6] == 1 and bingo[7] == 1 and bingo[8] == 1:
                return True
            if bingo[0] == 1 and bingo[3] == 1 and bingo[6] == 1:
                return True
            if bingo[1] == 1 and bingo[4] == 1 and bingo[7] == 1:
                return True
            if bingo[2] == 1 and bingo[5] == 1 and bingo[8] == 1:
                return True
            if bingo[0] == 1 and bingo[4] == 1 and bingo[8] == 1:
                return True
            if bingo[2] == 1 and bingo[4] == 1 and bingo[6] == 1:
                return True
            if A[i][j] in b:
                bingo[i * 3 + j] = 1
    return False
A = []
for i in range(3):
    A.append(list(map(int, input().split())))
N = int(input())
b = []
for i in range(N):
    b.append(int(input()))

if __name__ == '__main__':
    bingo()