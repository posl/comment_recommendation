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
            if j == H-1:
                print(A[j][i])
            else:
                print(A[j][i], end=' ')

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i in range(W):
        for j in range(H):
            print(A[j][i], end=' ')
        print()

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i in range(W):
        for j in range(H):
            print(A[j][i], end = " ")
        print()

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    for i in range(W):
        for j in range(H):
            print(A[j][i], end=" ")
        print()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for j in range(W):
        for i in range(H):
            print(A[i][j], end=' ')
        print()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0] * H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        print(' '.join(map(str, B[i])))

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            b[j][i] = a[i][j]
    for i in range(w):
        print(' '.join(map(str, b[i])))

=======
Suggestion 8

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(w):
        ans = []
        for j in range(h):
            ans.append(str(a[j][i]))
        print(" ".join(ans))

=======
Suggestion 9

def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

=======
Suggestion 10

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    # print(A)
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    # print(B)
    for i in range(W):
        print(*B[i])
    return 0
