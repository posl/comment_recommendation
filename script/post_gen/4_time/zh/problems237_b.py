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
            print(A[j][i], end=" ")
        print()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for j in range(W):
        B.append([])
        for i in range(H):
            B[j].append(A[i][j])
    for j in range(W):
        print(' '.join(map(str, B[j])))

=======
Suggestion 3

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(w):
        for j in range(h):
            print(a[j][i], end = " ")
        print()

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]

    for i in range(W):
        for j in range(H):
            B[i][j] = A[j][i]

    for i in range(W):
        for j in range(H):
            if j == H - 1:
                print(B[i][j])
            else:
                print(B[i][j], end=' ')

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0] * H for _ in range(W)]
    for i in range(W):
        for j in range(H):
            B[i][j] = A[j][i]
    for i in range(W):
        print(*B[i])

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))

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
                print(B[i][j],end=' ')

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    for i in range(w):
        for j in range(h):
            if j == h-1:
                print(a[j][i])
            else:
                print(a[j][i],end=" ")

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        for j in range(H):
            print(B[i][j],end=" ")
        print()
