def check_bingo(A):
    #縦のチェック
    for row in range(3):
        if A[row][0] == A[row][1] == A[row][2]:
            return True
    #横のチェック
    for col in range(3):
        if A[0][col] == A[1][col] == A[2][col]:
            return True
    #斜めのチェック
    if A[0][0] == A[1][1] == A[2][2]:
        return True
    if A[0][2] == A[1][1] == A[2][0]:
        return True
    return False
A = []
for row in range(3):
    A.append(list(map(int, input().split())))
N = int(input())
for _ in range(N):
    b = int(input())
    for row in range(3):
        for col in range(3):
            if A[row][col] == b:
                A[row][col] = 0
                break
    if check_bingo(A):
        print("Yes")
        exit()
print("No")
