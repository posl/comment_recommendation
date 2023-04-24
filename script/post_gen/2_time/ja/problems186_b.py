Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
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
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minA = 100
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    minA = 100
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    sum = 0
    for i in range(H):
        for j in range(W):
            sum += A[i][j] - min
    print(sum)
    return 0

=======
Suggestion 5

def main():
    # 標準入力の取得
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    # 処理
    min_a = 101
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    # 標準出力
    print(ans)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_a = 100
    for i in range(h):
        for j in range(w):
            min_a = min(min_a,a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 7

def solve():
    # 整数 1 つ
    #n = int(input())
    # 整数複数個
    h, w = map(int, input().split())
    # スペース区切り整数複数個
    #a, b = map(int, input().split())
    # 文字列 1 つ
    #s = input()
    # 文字列複数個
    #s = input().split()
    # 整数リスト
    #a = list(map(int, input().split()))
    # 整数リスト複数行
    #a = [int(input()) for _ in range(n)]
    # 整数リスト複数行複数列
    #a = [list(map(int, input().split())) for _ in range(n)]
    # 文字列リスト複数行
    #s = [input() for _ in range(n)]
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = 101
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])

    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a

    print(ans)

=======
Suggestion 8

def main():
    H,W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    minA = A[0][0]
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = 100000000
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_num:
                min_num = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_num
    print(ans)

=======
Suggestion 10

def get_ints(): return map(int, input().split())
