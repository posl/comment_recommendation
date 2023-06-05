Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(2)]
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

def problem255_a():
    R,C = map(int, input().split())
    A = []
    for i in range(2):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

=======
Suggestion 4

def main():
    r,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(2)]
    print(a[r-1][c-1])

=======
Suggestion 5

def problems255_a():
    R,C = map(int,input().split())
    a = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        a[i] = list(map(int,input().split()))
    print(a[R-1][C-1])

problems255_a()

=======
Suggestion 6

def main():
    r,c = map(int,input().split())
    a = []
    for i in range(2):
        a.append(list(map(int,input().split())))
    print(a[r-1][c-1])

=======
Suggestion 7

def problems255_a():
    r, c = map(int, input().split())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    print(a[r-1][c-1])

problems255_a()

=======
Suggestion 8

def problems255_a():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])

problems255_a()

=======
Suggestion 9

def problems255_a():
    r,c=map(int,input().split())
    a=[]
    for i in range(2):
        a.append(list(map(int,input().split())))
    print(a[r-1][c-1])
    return 0

=======
Suggestion 10

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])
