def main():
    bingo = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        bingo[i] = [int(j) for j in input().split()]
    N = int(input())
    b = [int(input()) for i in range(N)]
    for i in range(3):
        for j in range(3):
            for k in range(N):
                if bingo[i][j] == b[k]:
                    bingo[i][j] = 0
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
        print('Yes')
        return
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
        print('Yes')
        return
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0:
            print('Yes')
            return
    for j in range(3):
        if bingo[0][j] == bingo[1][j] == bingo[2][j] == 0:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()