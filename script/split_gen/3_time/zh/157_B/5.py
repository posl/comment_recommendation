def main():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    bingo = sum(bingo, [])
    n = int(input())
    for i in range(n):
        b = int(input())
        if b in bingo:
            bingo[bingo.index(b)] = 0
    if bingo[0] == bingo[1] == bingo[2] == 0 or bingo[3] == bingo[4] == bingo[5] == 0 or bingo[6] == bingo[7] == bingo[8] == 0 or bingo[0] == bingo[3] == bingo[6] == 0 or bingo[1] == bingo[4] == bingo[7] == 0 or bingo[2] == bingo[5] == bingo[8] == 0 or bingo[0] == bingo[4] == bingo[8] == 0 or bingo[2] == bingo[4] == bingo[6] == 0:
        print('Yes')
    else:
        print('No')
