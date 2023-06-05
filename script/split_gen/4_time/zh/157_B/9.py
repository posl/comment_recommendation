def bingo():
    #输入数据
    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        matrix[i] = list(map(int,input().split()))
    n = int(input())
    b = [0]*n
    for i in range(n):
        b[i] = int(input())
    #判断
    for i in range(3):
        if matrix[i][0] in b and matrix[i][1] in b and matrix[i][2] in b:
            return "Yes"
    for i in range(3):
        if matrix[0][i] in b and matrix[1][i] in b and matrix[2][i] in b:
            return "Yes"
    if matrix[0][0] in b and matrix[1][1] in b and matrix[2][2] in b:
        return "Yes"
    if matrix[0][2] in b and matrix[1][1] in b and matrix[2][0] in b:
        return "Yes"
    return "No"
