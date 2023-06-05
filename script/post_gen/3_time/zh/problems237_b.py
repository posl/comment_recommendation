Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(W):
        for j in range(H):
            B[i][j] = A[j][i]
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print("")

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for j in range(W):
        for i in range(H):
            if i != H - 1:
                print(A[i][j], end = " ")
            else:
                print(A[i][j], end = "\n")

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i in range(W):
        for j in range(H):
            if j < H - 1:
                print(A[j][i], end=' ')
            else:
                print(A[j][i], end='')
        print()

=======
Suggestion 4

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
Suggestion 5

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
            print(B[i][j], end=" ")
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

    for row in B:
        print(' '.join(map(str, row)))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            print(A[j][i], end=' ')
        print()

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i in range(W):
        for j in range(H):
            print(A[j][i], end=' ')
        print('')

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
        print()

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        for j in range(h):
            print(a[j][i], end=' ')
        print()
