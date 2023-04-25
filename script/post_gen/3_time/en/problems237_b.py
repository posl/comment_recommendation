Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i in range(W):
        for j in range(H):
            print(A[j][i], end=" ")
        print()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        for j in range(H):
            print(A[j][i], end=' ')
        print()

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    for i in range(w):
        for j in range(h):
            print(a[j][i], end=" ")
        print("")

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for w in range(W):
        for h in range(H):
            print(A[h][w], end=' ')
        print()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    for i in range(W):
        for j in range(H):
            print(A[j][i], end=" ")
        print()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(B[i][j])
            else:
                print(B[i][j], end=' ')

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0] * H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        print(*B[i])

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(x) for x in zip(*a)]
    for i in range(w):
        for j in range(h):
            print(b[i][j], end=' ')
        print()

=======
Suggestion 9

def main():
    # input
    H, W = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]

    # compute

    # output
    for w in range(W):
        for h in range(H):
            print(A[h][w], end=' ')
        print()

=======
Suggestion 10

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
