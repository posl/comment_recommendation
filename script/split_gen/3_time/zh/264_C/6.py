def solve():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    # 二维数组的行和列的删除
    # 二维数组的行和列的删除
    def delete_row_col(A, row, col):
        # 删除行
        A.pop(row)
        # 删除列
        for i in range(len(A)):
            A[i].pop(col)
        return A
    # 判断二维数组是否相等
    def is_equal(A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != B[i][j]:
                    return False
        return True
    # 判断是否可以使A等于B
    def is_equal(A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != B[i][j]:
                    return False
        return True
    # 从A中删除行和列，使A等于B
    def delete_row_col(A, B):
        while len(A) > len(B):
            A.pop()
        while len(A[0]) > len(B[0]):
            for i in range(len(A)):
                A[i].pop()
        return A
    # 判断是否可以使A等于B
    def is_equal(A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != B[i][j]:
                    return False
        return True
    for i in range(H1):
        for j in range(W1):
            A = delete_row_col(A, i, j)
            if is_equal(A, B):
                print("Yes")
                return
            A = [list(map(int, input().split())) for _ in range(H1)]
    print("No")
