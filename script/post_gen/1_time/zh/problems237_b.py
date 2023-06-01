Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(B[i][j])
            else:
                print(B[i][j], end=' ')

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    B = [[0] * H for i in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        print(*B[i])

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    B = [[0 for i in range(H)] for j in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print()

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    for i in range(w):
        for j in range(h):
            if j == h - 1:
                print(a[j][i])
            else:
                print(a[j][i], end=' ')

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(A[j][i])
            else:
                print(A[j][i],end=' ')

=======
Suggestion 7

def main():
    #输入矩阵的行数和列数
    n, m = map(int, input().split())
    #输入矩阵
    A = [list(map(int, input().split())) for i in range(n)]
    #转置矩阵
    B = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    #输出矩阵
    for i in range(m):
        for j in range(n):
            print(B[i][j], end=" ")
        print()

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(w):
        for j in range(h):
            print(a[j][i], end=" ")
        print()

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=' ')
        print('')
