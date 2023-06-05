def main():
    bingo = [[],[],[]]
    for i in range(3):
        bingo[i] = list(map(int, input().split()))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            for k in range(N):
                if bingo[i][j] == b[k]:
                    bingo[i][j] = 0
    ans = 'No'
    for i in range(3):
        if bingo[i][0] == 0 and bingo[i][1] == 0 and bingo[i][2] == 0:
            ans = 'Yes'
        if bingo[0][i] == 0 and bingo[1][i] == 0 and bingo[2][i] == 0:
            ans = 'Yes'
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0:
        ans = 'Yes'
    if bingo[0][2] == 0 and bingo[1][1] == 0 and bingo[2][0] == 0:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()