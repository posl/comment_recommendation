Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    r,c = input().split()
    r = int(r)
    c = int(c)
    A = []
    for i in range(2):
        A.append(input().split())
        A[i][0] = int(A[i][0])
        A[i][1] = int(A[i][1])
    print(A[r-1][c-1])

=======
Suggestion 2

def main():
    r,c = map(int,input().split())
    a = []
    for i in range(2):
        a.append(list(map(int,input().split())))
    print(a[r-1][c-1])

=======
Suggestion 3

def get_matrix_value(r, c, matrix):
    return matrix[r-1][c-1]

=======
Suggestion 4

def main():
    r, c = map(int, input().split())
    a = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        a[i] = list(map(int, input().split()))
    print(a[r-1][c-1])

=======
Suggestion 5

def solve():
    R, C = map(int, input().split())
    A = []
    for i in range(2):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

solve()

=======
Suggestion 6

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 7

def get_matrix():
    r,c = map(int, input().split())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    print(a[r-1][c-1])

=======
Suggestion 8

def print_matrix_element():
    r, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(2)]
    print(matrix[r-1][c-1])

=======
Suggestion 9

def main():
    r,c=map(int,input().split())
    a=[list(map(int,input().split())) for i in range(2)]
    print(a[r-1][c-1])

=======
Suggestion 10

def print_matrix_element():
    R, C = map(int, input().split())
    A = []
    for i in range(R):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])
