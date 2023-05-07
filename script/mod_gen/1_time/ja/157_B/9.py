def bingo():
    # 垂直方向に揃っているかを判定
    for i in range(3):
        if (A[0][i] == A[1][i] == A[2][i]):
            return True
    # 水平方向に揃っているかを判定
    for i in range(3):
        if (A[i][0] == A[i][1] == A[i][2]):
            return True
    # 斜め方向に揃っているかを判定
    if (A[0][0] == A[1][1] == A[2][2]):
        return True
    if (A[0][2] == A[1][1] == A[2][0]):
        return True
    return False
A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k] = 0

if __name__ == '__main__':
    bingo()