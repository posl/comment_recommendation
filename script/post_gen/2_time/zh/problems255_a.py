Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R,C = map(int,input().split())
    A = []
    for i in range(2):
        A.append(list(map(int,input().split())))
    print(A[R-1][C-1])

=======
Suggestion 2

def main():
    r,c = map(int,raw_input().split())
    A = []
    for i in range(2):
        A.append(map(int,raw_input().split()))
    print A[r-1][c-1]

=======
Suggestion 3

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 4

def solve():
    r,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(2)]
    print(a[r-1][c-1])
solve()

=======
Suggestion 5

def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])
main()

=======
Suggestion 6

def solve():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[R - 1][C - 1])

=======
Suggestion 7

def problems255_a():
    r,c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(2)]
    print(a[r-1][c-1])

=======
Suggestion 8

def problems255_a():
    r,c = map(int,input().split())
    a = []
    for i in range(2):
        a.append(list(map(int,input().split())))
    print(a[r-1][c-1])

problems255_a()
