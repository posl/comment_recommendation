Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 2

def main():
    r,c = map(int,input().split())
    matrix = []
    for i in range(2):
        matrix.append(list(map(int,input().split())))
    print(matrix[r-1][c-1])

=======
Suggestion 3

def problems255_a():
    R, C = map(int, input().split())
    A = []
    for i in range(2):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

=======
Suggestion 4

def getRC():
    RC = input().split()
    return int(RC[0]), int(RC[1])

=======
Suggestion 5

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 6

def main():
    R,C = map(int, input().split())
    A = []
    for i in range(2):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

=======
Suggestion 7

def main():
    r,c = map(int,input().split())
    A = []
    for i in range(2):
        A.append(list(map(int,input().split())))
    print(A[r-1][c-1])

=======
Suggestion 8

def main():
    # 读取输入
    R, C = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(2)]
    # 算法
    print(A[R - 1][C - 1])

=======
Suggestion 9

def problems255_a():
    R,C = map(int,input().split())
    A = []
    for i in range(2):
        A.append(list(map(int,input().split())))
    print(A[R-1][C-1])


problems255_a()
