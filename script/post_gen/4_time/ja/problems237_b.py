Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(A[j][i], end="")
            else:
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
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        print(' '.join(map(str, B[i])))

=======
Suggestion 3

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
        print(*B[i])

=======
Suggestion 4

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
Suggestion 5

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
                print(A[j][i],end=" ")

=======
Suggestion 6

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
        print(*B[j])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    B = [[0 for i in range(H)] for j in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        print(*B[i])

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    b = [[0] * h for i in range(w)]
    for i in range(h):
        for j in range(w):
            b[j][i] = a[i][j]
    for i in range(w):
        print(*b[i])

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    #print(a)
    b = []
    for i in range(w):
        b.append([])
        for j in range(h):
            b[i].append(a[j][i])
    #print(b)
    for i in range(w):
        print(*b[i])
