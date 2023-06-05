def main():
    matrix = []
    for i in range(3):
        matrix.append(list(map(int, input().split())))
    N = int(input())
    bingo = []
    for i in range(N):
        bingo.append(int(input()))
    flag = 0
    for i in range(3):
        if matrix[0][i] in bingo and matrix[1][i] in bingo and matrix[2][i] in bingo:
            flag = 1
            break
    for i in range(3):
        if matrix[i][0] in bingo and matrix[i][1] in bingo and matrix[i][2] in bingo:
            flag = 1
            break
    if matrix[0][0] in bingo and matrix[1][1] in bingo and matrix[2][2] in bingo:
        flag = 1
    if matrix[0][2] in bingo and matrix[1][1] in bingo and matrix[2][0] in bingo:
        flag = 1
    if flag == 1:
        print("Yes")
    else:
        print("No")
main()
