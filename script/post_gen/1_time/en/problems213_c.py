Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    pos = dict()
    for i in range(N):
        pos[A[i] * 1000000001 + B[i]] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if i * 1000000001 + j not in pos:
                print(i, j)

=======
Suggestion 2

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

main()

=======
Suggestion 3

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # サンプル 2 の場合、H と W が大きいため、
    # 配列を作るとメモリエラーになる。
    # そのため、配列を作らずに、
    # ソートした後に、同じ値が連続している数をカウントする。
    # これを用いて、A, B の値を更新する。
    A.sort()
    B.sort()
    A.append(H + 1)
    B.append(W + 1)
    A_cnt = 1
    B_cnt = 1
    for i in range(N):
        if A[i] == A[i + 1]:
            A_cnt += 1
        else:
            A[i] = A_cnt
            A_cnt = 1
        if B[i] == B[i + 1]:
            B_cnt += 1
        else:
            B[i] = B_cnt
            B_cnt = 1

    for i in range(N):
        print(A[i], B[i])

=======
Suggestion 4

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # ここから書きましょう
    C = [0] * N
    D = [0] * N
    # ここまで書きましょう
    for i in range(N):
        print(C[i], D[i])

=======
Suggestion 5

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    ans = []
    for i in range(N):
        ans.append([A.index(A[i])+1, B.index(B[i])+1])
    for i in range(N):
        print(ans[i][0], ans[i][1])

=======
Suggestion 6

def main():
    h, w, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    a = sorted(a)
    b = sorted(b)

    for i in range(n):
        print(a.index(a[i]) + 1, b.index(b[i]) + 1)

=======
Suggestion 7

def main():
    h, w, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i)
    for k in d:
        d[k].sort(key=lambda i: b[i])
    ans = [(0, 0)] * n
    for i in range(n):
        ans[i] = (len(d) + 1 - a[i], len(d[a[i]]) + 1 - b[i])
    ans.sort()
    for i in range(n):
        print(ans[i][0], ans[i][1])

=======
Suggestion 8

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    for i in range(n):
        print(a.index(a[i]) + 1, b.index(b[i]) + 1)

=======
Suggestion 9

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i
    for i in range(len(b)):
        b_dict[b[i]] = i
    for i in range(n):
        print(a_dict[a[i]] + 1, b_dict[b[i]] + 1)

=======
Suggestion 10

def main():
    H,W,N = map(int,input().split())
    A = []
    B = []
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i])+1,B.index(B[i])+1)
