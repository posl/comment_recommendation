def main():
    #输入矩阵的行数和列数
    n, m = map(int, input().split())
    #输入矩阵
    A = [list(map(int, input().split())) for i in range(n)]
    #转置矩阵
    B = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    #输出矩阵
    for i in range(m):
        for j in range(n):
            print(B[i][j], end=" ")
        print()
