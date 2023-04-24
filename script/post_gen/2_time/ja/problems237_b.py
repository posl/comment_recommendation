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
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        print(*[A[j][i] for j in range(H)])

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        print(*[a[j][i] for j in range(h)])

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[0 for i in range(H)] for j in range(W)]

    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]

    for i in range(W):
        print(*B[i])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [input().split() for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print()

=======
Suggestion 6

def main():
    #入力
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    
    #転置行列を求める
    B = []
    for i in range(W):
        B.append([A[j][i] for j in range(H)])
    
    #出力
    for i in range(W):
        print(*B[i])

main()

=======
Suggestion 7

def main():
    #入力
    H, W = map(int, input().split())
    #A = [list(map(int, input().split())) for i in range(H)]
    A = [input().split() for i in range(H)]
    #B = [[0]*H for i in range(W)]
    #転置行列を作成
    B = list(zip(*A))
    #出力
    for i in range(W):
        print(" ".join(B[i]))
