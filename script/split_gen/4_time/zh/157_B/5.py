def bingo():
    # 读取输入
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    # 算法
    # 横向
    for i in range(3):
        if A[i][0] in b and A[i][1] in b and A[i][2] in b:
            return 'Yes'
    # 纵向
    for i in range(3):
        if A[0][i] in b and A[1][i] in b and A[2][i] in b:
            return 'Yes'
    # 斜向
    if A[0][0] in b and A[1][1] in b and A[2][2] in b:
        return 'Yes'
    if A[0][2] in b and A[1][1] in b and A[2][0] in b:
        return 'Yes'
    # 其他
    return 'No'
print(bingo())
