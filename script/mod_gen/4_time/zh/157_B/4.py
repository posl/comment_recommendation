def main():
    # 读入数据
    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        matrix[i] = list(map(int, input().split()))
    n = int(input())
    b = [0 for i in range(n)]
    for i in range(n):
        b[i] = int(input())
    # 处理数据
    for i in range(3):
        for j in range(3):
            for k in range(n):
                if matrix[i][j] == b[k]:
                    matrix[i][j] = 0
                    break
    # 判断是否有宾果
    bingo = False
    for i in range(3):
        if matrix[i][0] == 0 and matrix[i][1] == 0 and matrix[i][2] == 0:
            bingo = True
            break
        if matrix[0][i] == 0 and matrix[1][i] == 0 and matrix[2][i] == 0:
            bingo = True
            break
    if matrix[0][0] == 0 and matrix[1][1] == 0 and matrix[2][2] == 0:
        bingo = True
    if matrix[0][2] == 0 and matrix[1][1] == 0 and matrix[2][0] == 0:
        bingo = True
    # 输出结果
    if bingo:
        print("Yes")
    else:
        print("No")
main()
