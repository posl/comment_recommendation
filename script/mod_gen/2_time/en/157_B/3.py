def main():
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    B = [int(input()) for i in range(N)]
    bingo = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(N):
                if A[i][j] == B[k]:
                    bingo[i][j] = 1
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 1:
            print('Yes')
            return
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == 1:
            print('Yes')
            return
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 1:
        print('Yes')
        return
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 1:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()