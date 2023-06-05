def main():
    #读取数据
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    #判断是否有宾果
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 0
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] == 0:
            print('Yes')
            exit()
    for i in range(3):
        if A[0][i] == A[1][i] == A[2][i] == 0:
            print('Yes')
            exit()
    if A[0][0] == A[1][1] == A[2][2] == 0:
        print('Yes')
        exit()
    if A[0][2] == A[1][1] == A[2][0] == 0:
        print('Yes')
        exit()
    print('No')
    return
