Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 2

def main():
    R, C = map(int, input().split())
    A = []
    for i in range(2):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

=======
Suggestion 3

def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 5

def main():
    r,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(2)]
    print(a[r-1][c-1])

=======
Suggestion 6

def main():
    R, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(2)]
    print(matrix[R-1][C-1])

=======
Suggestion 7

def main():
    a = [list(map(int, input().split())) for _ in range(2)]
    r, c = map(int, input().split())
    print(a[r-1][c-1])

=======
Suggestion 8

def main():
    # R,Cを入力
    R,C = map(int,input().split())
    # Aの行列を入力
    A = [list(map(int,input().split())) for i in range(2)]
    # AのR,Cの要素を出力
    print(A[R-1][C-1])
