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
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2)]
    print(a[r-1][c-1])

=======
Suggestion 3

def main():
    r, c = map(int, input().split())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    print(a[r-1][c-1])

=======
Suggestion 4

def main():
    r, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(2)]
    print(matrix[r-1][c-1])
