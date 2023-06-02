Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r,c = map(int,input().split())
    a = []
    for i in range(2):
        a.append(list(map(int,input().split())))
    print(a[r-1][c-1])

=======
Suggestion 2

def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 3

def main():
    R,C = map(int,input().split())
    A = []
    for i in range(2):
        A.append(list(map(int,input().split())))
    print(A[R-1][C-1])

=======
Suggestion 4

def problems255_a():
    R,C = map(int,input().split())
    A = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        A[i] = list(map(int,input().split()))
    print(A[R-1][C-1])

=======
Suggestion 5

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])
main()

=======
Suggestion 6

def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[R-1][C-1])
