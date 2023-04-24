Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            print(A[j][i], end = ' ')
        print()

main()

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for row in B:
        print(*row)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    for j in range(W):
        for i in range(H):
            if i == H - 1:
                print(A[i][j])
            else:
                print(A[i][j], end=' ')

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        print(' '.join([str(A[j][i]) for j in range(H)]))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    for i in range(W):
        print(' '.join(map(str, [A[j][i] for j in range(H)])))

=======
Suggestion 8

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

=======
Suggestion 9

def transpose_matrix(matrix):
    #transpose matrix
    return list(map(list, zip(*matrix)))
