Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i + 1
    for i in range(len(b)):
        b_dict[b[i]] = i + 1
    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])

=======
Suggestion 3

def main():
    h, w, n = map(int, input().split())
    # print(h, w, n)

    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))

    # print(ab)

    # 1. 生成一个h*w的矩阵
    # 2. 依次填入ab中的数字
    # 3. 从上往下，从左往右，填入数字，如果有数字，就跳过
    # 4. 如果某一行或者某一列没有数字，就把这一行或者这一列的数字都清空，然后把剩下的数字往上或者往左移动，填补空缺
    # 5. 重复3，4

    matrix = [[0 for _ in range(w)] for _ in range(h)]
    # print(matrix)

    for i in range(n):
        a, b = ab[i]
        matrix[a-1][b-1] = i + 1

    # print(matrix)

    # 从上往下
    for i in range(h):
        # 从左往右
        for j in range(w):
            if matrix[i][j] == 0:
                continue
            else:
                print(i+1, j+1)

=======
Suggestion 4

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    #print(h)
    #print(w)
    #print(n)
    #print(a[0])
    #print(b[0])
    #print(a[1])
    #print(b[1])
    #print(a[2])
    #print(b[2])
    #print(a[3])
    #print(b[3])
    #print(a[4])
    #print(b[4])
    #print(a[5])
    #print(b[5])
    #print(a[6])
    #print(b[6])
    #print(a[7])
    #print(b[7])
    #print(a[8])
    #print(b[8])
    #print(a[9])
    #print(b[9])
    #print(a[10])
    #print(b[10])
    #print(a[11])
    #print(b[11])
    #print(a[12])
    #print(b[12])
    #print(a[13])
    #print(b[13])
    #print(a[14])
    #print(b[14])
    #print(a[15])
    #print(b[15])
    #print(a[16])
    #print(b[16])
    #print(a[17])
    #print(b[17])
    #print(a[18])
    #print(b[18])
    #print(a[19])
    #print(b[19])
    #print(a[20])
    #print(b[20])
    #print(a[21])
    #print(b[21])
    #print(a[22])
    #print(b[22])
    #print(a[23])
    #print(b[23])
    #print(a[24])
    #print(b[24])
    #print(a[25])
    #print(b[25])
    #print(a[26])
    #print(b[26])
    #print(a[27])
    #print(b[27])
    #print(a[28])
    #print(b[28])
    #print(a[29])
    #print(b[29])

=======
Suggestion 5

def main():
    h,w,n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i+1
    for i in range(len(b)):
        b_dict[b[i]] = i+1
    for i in range(n):
        print(a_dict[a[i]], b_dict[b[i]])

=======
Suggestion 6

def main():
    H,W,N = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(H,W,N)
    # print(A,B)
    # print(type(A),type(B))
    # print(type(H),type(W),type(N))
    # print(type(A[0]),type(B[0]))
    # print(len(A),len(B))
    # print(A[0],B[0])
    # print(A[0],B[0])
    # print(A[1],B[1])
    # print(A[2],B[2])
    # print(A[3],B[3])
    # print(A[4],B[4])
    # print(A[5],B[5])
    # print(A[6],B[6])
    # print(A[7],B[7])
    # print(A[8],B[8])
    # print(A[9],B[9])
    # print(A[10],B[10])
    # print(A[11],B[11])
    # print(A[12],B[12])
    # print(A[13],B[13])
    # print(A[14],B[14])
    # print(A[15],B[15])
    # print(A[16],B[16])
    # print(A[17],B[17])
    # print(A[18],B[18])
    # print(A[19],B[19])
    # print(A[20],B[20])
    # print(A[21],B[21])
    # print(A[22],B[22])
    # print(A[23],B[23])
    # print(A[24],B[24])
    # print(A[25],B[25])
    # print(A[26],B[26])
    # print(A[27],B[27])
    # print(A[28],B[28])
    # print(A[29],B[29])
    # print(A[30],B[30])
    # print(A[31],B[31])
    # print(A[32],B[32])
    # print(A[33],B[33])

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # print(H, W, N)
    # print(A)
    # print(B)

    # 要用set，否则会超时
    setA = set(A)
    setB = set(B)

    # print(setA)
    # print(setB)

    # 把set转换成list，否则会超时
    listA = list(setA)
    listB = list(setB)

    # print(listA)
    # print(listB)

    # listA.sort()
    # listB.sort()

    # print(listA)
    # print(listB)

    dictA = {}
    dictB = {}

    for i in range(len(listA)):
        dictA[listA[i]] = i + 1

    for i in range(len(listB)):
        dictB[listB[i]] = i + 1

    # print(dictA)
    # print(dictB)

    for i in range(N):
        print(dictA[A[i]], dictB[B[i]])

=======
Suggestion 8

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(H)
    #print(W)
    #print(N)
    #print(A[0])
    #print(B[0])
    #print(A[1])
    #print(B[1])
    #print(A[2])
    #print(B[2])
    #print(A[3])
    #print(B[3])
    #print(A[4])
    #print(B[4])
    #print(A[5])
    #print(B[5])
    #print(A[6])
    #print(B[6])
    #print(A[7])
    #print(B[7])
    #print(A[8])
    #print(B[8])
    #print(A[9])
    #print(B[9])
    #print(A[10])
    #print(B[10])
    #print(A[11])
    #print(B[11])
    #print(A[12])
    #print(B[12])
    #print(A[13])
    #print(B[13])
    #print(A[14])
    #print(B[14])
    #print(A[15])
    #print(B[15])
    #print(A[16])
    #print(B[16])
    #print(A[17])
    #print(B[17])
    #print(A[18])
    #print(B[18])
    #print(A[19])
    #print(B[19])
    #print(A[20])
    #print(B[20])
    #print(A[21])
    #print(B[21])
    #print(A[22])
    #print(B[22])
    #print(A[23])
    #print(B[23])
    #print(A[24])
    #print(B[24])
    #print(A[25])
    #print(B[25])
    #print(A[26])
    #print(B[26])
    #print(A[27])
    #print(B[27])
    #print(A[28])
    #print(B[28])
    #print(A[29])
    #print(B[29])
    #
