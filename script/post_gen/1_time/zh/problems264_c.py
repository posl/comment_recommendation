Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    # H_1 W_1
    # A_{1, 1} A_{1, 2} ...A_{1, W_1}
    # A_{2, 1} A_{2, 2} ...A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ...A_{H_1, W_1}.
    # H_2 W_2
    # B_{1, 1} B_{1, 2} ...B_{1, W_2}
    # B_{2, 1} B_{2, 2} ...B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ...B_{H_2, W_2}
    h_1, w_1 = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h_1)]
    h_2, w_2 = map(int, input().split())
    b = [list(map(int, input().split())) for i in range(h_2)]
    for i in range(h_1 - h_2 + 1):
        for j in range(w_1 - w_2 + 1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h_2):
                    for l in range(w_2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                if flag:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 3

def main():
    h1,w1 = map(int,input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int,input().split())))
    h2,w2 = map(int,input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int,input().split())))
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            flag = False
                            break
                if flag:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 4

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for i in range(h2)]

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 5

def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    # print(A, B)
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            # print(i, j)
            if A[i][j] == B[0][0]:
                # print(i, j)
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if A[i+k][j+l] != B[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 6

def main():
    h1,w1 = map(int,input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int,input().split())))
    h2,w2 = map(int,input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int,input().split())))
    #print(A)
    #print(B)
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            #print("i:{},j:{}".format(i,j))
            #print(A[i][j:j+w2])
            #print(B[0])
            if A[i][j:j+w2] == B[0]:
                #print("A[i][j:j+w2]:{}".format(A[i][j:j+w2]))
                #print("B[0]:{}".format(B[0]))
                #print("A[i][j:j+w2] == B[0]:{}".format(A[i][j:j+w2] == B[0]))
                for k in range(1,h2):
                    #print("A[i+k][j:j+w2]:{}".format(A[i+k][j:j+w2]))
                    #print("B[k]:{}".format(B[k]))
                    #print("A[i+k][j:j+w2] == B[k]:{}".format(A[i+k][j:j+w2] == B[k]))
                    if A[i+k][j:j+w2] != B[k]:
                        break
                else:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 7

def matrix_equal():
    h1,w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2,w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1):
        for j in range(w1):
            if i+h2 > h1 or j+w2 > w1:
                continue
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            flag = False
                if flag:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    h1, w1 = map(int, input().split())
    a = []
    for _ in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for _ in range(h2):
        b.append(list(map(int, input().split())))
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 9

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    if H1<H2 or W1<W2:
        print("No")
        return
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                flag = 1
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l] != B[k][l]:
                            flag = 0
                            break
                    if flag == 0:
                        break
                if flag == 1:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 10

def main():
    # 读入矩阵A
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    # 读入矩阵B
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    # 从矩阵A中删除行和列，使其等于矩阵B
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            # 从矩阵A中删除行和列，使其等于矩阵B
            for k in range(h2):
                if a[i + k][j:j + w2] != b[k]:
                    break
            else:
                print('Yes')
                exit()
    print('No')
