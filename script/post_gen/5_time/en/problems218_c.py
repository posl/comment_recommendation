Synthesizing 10/10 solutions

=======
Suggestion 1

def is_same(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i][j] != list2[i][j]:
                return False
    return True

=======
Suggestion 2

def match(S, T):
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] != T[i][j]:
                return False
    return True

=======
Suggestion 3

def rotate90(a):
    n = len(a)
    b = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[j][n-1-i] = a[i][j]
    return b

=======
Suggestion 4

def rotate90(list):
    result = []
    for i in range(len(list[0])):
        tmp = []
        for j in range(len(list)):
            tmp.append(list[j][i])
        tmp.reverse()
        result.append(tmp)
    return result

=======
Suggestion 5

def rotate_clockwise(matrix):
    """Rotates a matrix clockwise"""
    return [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]

=======
Suggestion 6

def rotate90(matrix):
    return [list(x) for x in zip(*matrix[::-1])]

=======
Suggestion 7

def rotate_matrix_90(m):
    return list(zip(*m[::-1]))

=======
Suggestion 8

def rotate90(matrix):
    return list(zip(*matrix[::-1]))

=======
Suggestion 9

def rotate90(grid):
    return list(zip(*grid[::-1]))

=======
Suggestion 10

def rotate(image):
    image = zip(*image[::-1])
    return image
