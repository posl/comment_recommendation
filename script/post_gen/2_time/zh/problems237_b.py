Synthesizing 10/10 solutions

=======
Suggestion 1

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

=======
Suggestion 2

def main():
    # H, W = map(int, input().split())
    # for i in range(H):
    #     A = list(map(int, input().split()))
    #     print(A)
    #     for j in range(W):
    #         B = A[j][i]
    #         print(B)
    #         print(' '.join(map(str, B)))
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            B = A[j][i]
            print(B)
        print(' '.join(map(str, B)))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            if j == H - 1:
                print(A[j][i])
            else:
                print(A[j][i], end=' ')

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(w):
        for j in range(h):
            if j == h - 1:
                print(a[j][i])
            else:
                print(a[j][i], end = ' ')

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for j in range(W):
        for i in range(H):
            if i == H - 1:
                print(A[i][j])
            else:
                print(A[i][j], end=" ")

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    for i in range(w):
        for j in range(h):
            if j == h - 1:
                print(a[j][i])
            else:
                print(a[j][i], end=" ")

=======
Suggestion 7

def main():
    h, w = [int(i) for i in input().split()]
    a = []
    for _ in range(h):
        a.append([int(i) for i in input().split()])
    for i in range(w):
        for j in range(h):
            print(a[j][i], end=' ')
        print()

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        for j in range(h):
            print(a[j][i], end=' ')
        print()

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    for i in range(W):
        for j in range(H):
            print(A[j][i], end=" ")
        print()
    return 0

=======
Suggestion 10

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    for j in range(w):
        for i in range(h):
            if i == h-1:
                print(a[i][j])
            else:
                print(a[i][j],end=' ')
