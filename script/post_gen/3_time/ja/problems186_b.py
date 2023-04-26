Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    s = 0
    for i in range(H):
        for j in range(W):
            s += A[i][j]

    print(s - H * W * min(map(min, A)))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_A = 100
    for i in range(H):
        for j in range(W):
            min_A = min(min_A, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    minA = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < minA:
                minA = A[i][j]

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA

    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_A = 101
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_A:
                min_A = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    min_a = 100
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 6

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min([min(a) for a in A])
    print(sum([sum(a) - min_A * W for a in A]))

=======
Suggestion 7

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_a = min([min(a) for a in A])
    ans = 0
    for a in A:
        for aa in a:
            ans += aa - min_a
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minA = min([min(a) for a in A])
    ans = 0
    for a in A:
        for b in a:
            ans += b - minA
    print(ans)

=======
Suggestion 9

def main():
    h,w=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(h)]
    min_a=float('inf')
    for i in range(h):
        for j in range(w):
            min_a=min(min_a,a[i][j])
    ans=0
    for i in range(h):
        for j in range(w):
            ans+=a[i][j]-min_a
    print(ans)

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # まずは各行の合計値を求める
    sum_row = [0] * H
    for i in range(H):
        sum_row[i] = sum(A[i])

    # 各列の合計値を求める
    sum_col = [0] * W
    for i in range(W):
        for j in range(H):
            sum_col[i] += A[j][i]

    # 各マスのブロックの数を求める
    sum_all = sum(sum_row)
    sum_each = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            sum_each[i][j] = sum_all - sum_row[i] - sum_col[j] + A[i][j]

    # 各マスを全て同じ値にするために必要なブロックの数を求める
    ans = 10 ** 9
    for i in range(H):
        for j in range(W):
            ans = min(ans, sum_each[i][j])

    print(ans)
