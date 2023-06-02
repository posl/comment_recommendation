Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate90(S):
    S90 = []
    for i in range(len(S)):
        temp = ''
        for j in range(len(S)):
            temp += S[j][i]
        S90.append(temp[::-1])
    return S90

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    # print(s)
    # print(t)
    s = rotate(s)
    # print(s)
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def rotate_90_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    res = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-1-i] = matrix[i][j]
    return res

=======
Suggestion 4

def rotate90(S):
    N = len(S)
    S2 = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            S2[N-1-j][i] = S[i][j]
    return S2

=======
Suggestion 5

def get_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    return matrix

=======
Suggestion 6

def get_rotate_matrix(matrix):
    """
    顺时针旋转矩阵90度
    :param matrix: list[list[]]
    :return:
    """
    n = len(matrix)
    rotate_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_matrix[i][j] = matrix[n - 1 - j][i]
    return rotate_matrix

=======
Suggestion 7

def rotate90(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0])-1,-1,-1)]

=======
Suggestion 8

def rotate90(S):
    N = len(S)
    T = [['.' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            T[i][j] = S[N-1-j][i]
    return T

=======
Suggestion 9

def rotate(matrix):
    return list(zip(*matrix[::-1]))

=======
Suggestion 10

def rotate_90(matrix):
    return list(zip(*matrix[::-1]))
