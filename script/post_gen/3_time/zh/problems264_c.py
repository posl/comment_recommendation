Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h1,w1=map(int,input().split())
    a=[]
    for i in range(h1):
        a.append(list(map(int,input().split())))
    h2,w2=map(int,input().split())
    b=[]
    for i in range(h2):
        b.append(list(map(int,input().split())))
    if h1<h2 or w1<w2:
        print("No")
    else:
        for i in range(h1-h2+1):
            for j in range(w1-w2+1):
                if a[i][j]==b[0][0]:
                    flag=True
                    for k in range(h2):
                        for l in range(w2):
                            if a[i+k][j+l]!=b[k][l]:
                                flag=False
                                break
                        if not flag:
                            break
                    if flag:
                        print("Yes")
                        return
        print("No")
    return

=======
Suggestion 2

def main():
    # 读取数据
    h1, w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))

    # 从a中删除h2行w2列
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            # 从a中删除h2行w2列
            c = [a[i + k][j:j + w2] for k in range(h2)]
            # 判断c是否等于b
            if c == b:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            for k in range(H2):
                for l in range(W2):
                    if A[i + k][j + l] != B[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return
    print("No")

=======
Suggestion 5

def main():
    h1,w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int,input().split())))
    h2,w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int,input().split())))
    if h1 < h2 or w1 < w2:
        print("No")
        exit()
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            for k in range(h2):
                for l in range(w2):
                    if a[i+k][j+l] != b[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                exit()
    print("No")
    exit()

=======
Suggestion 6

def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if A[i][j] == B[0][0]:
                if A[i:h2 + i] == B:
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 7

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
