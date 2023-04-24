Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #問題文
    #H 行 W 列の行列 A が与えられます。
    #A の上から i 行目、左から j 列目の要素は A_{i,j} です。   
    #ここで、W 行 H 列の行列 B を、上から i 行目、左から j 列目の要素が A_{j,i} と一致するような行列として定めます。
    #すなわち、B は A の転置行列です。  
    #B を出力してください。
    #
    #制約
    #1≦ H,W ≦ 10^5
    #H × W ≦ 10^5
    #1 ≦ A_{i,j} ≦ 10^9
    #入力は全て整数である
    #
    #入力
    #入力は以下の形式で標準入力から与えられる。
    #H W
    #A_{1,1} A_{1,2} ... A_{1,W}
    #A_{2,1} A_{2,2} ... A_{2,W}
    #.
    #.
    #.
    #A_{H,1} A_{H,2} ... A_{H,W}
    #
    #出力
    #B を以下の形式で出力せよ。  
    #B_{1,1} B_{1,2} ... B_{1,H}
    #B_{2,1} B_{2,2} ... B_{2,H}
    #.
    #.
    #.
    #B_{W,1} B_{W,2} ... B_{W,H}
    #
    #入力例 1
    #4 3
    #1 2 3
    #4 5 6
    #7 8 9
    #10 11 12
    #
    #出力例 1
    #1 4 7 10
    #2 5 8 11
    #3 6 9 12
    #たとえ

=======
Suggestion 2

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
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for j in range(W):
        for i in range(H):
            print(A[i][j], end="")
            if i == H-1:
                print()
            else:
                print(" ", end="")

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        for j in range(h):
            print(a[j][i], end="")
            if j != h-1:
                print(" ", end="")
        print()

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for i in range(W):
        print(*B[i])

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for j in range(w):
        print(*[a[i][j] for i in range(h)])

=======
Suggestion 7

def main():
    #入力
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    #転置行列
    B = [[0 for i in range(H)] for j in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]

    #出力
    for i in range(W):
        for j in range(H):
            print(B[i][j], end=" ")
        print()

=======
Suggestion 8

def main():
    #入力
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    #転置行列
    B = [[0 for i in range(H)] for j in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    #出力
    for i in range(W):
        for j in range(H):
            print(B[i][j],end="")
            if j == H-1:
                print()
            else:
                print(" ",end="")
