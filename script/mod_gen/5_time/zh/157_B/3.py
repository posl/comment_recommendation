def main():
    # 读取输入
    A = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        A[i] = list(map(int, input().split()))
    N = int(input())
    b = [0 for i in range(N)]
    for i in range(N):
        b[i] = int(input())
    # 处理
    bingo = False
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 0
    for i in range(3):
        if A[i][0] == 0 and A[i][1] == 0 and A[i][2] == 0:
            bingo = True
        if A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
            bingo = True
    if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
        bingo = True
    if A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
        bingo = True
    # 输出
    if bingo:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()