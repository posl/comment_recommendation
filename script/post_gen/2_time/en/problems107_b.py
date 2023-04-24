Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    row = [False] * h
    col = [False] * w
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True
    for i in range(h):
        if row[i]:
            for j in range(w):
                if col[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    h = [False for _ in range(H)]
    w = [False for _ in range(W)]
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                h[i] = True
                w[j] = True
    for i in range(H):
        if h[i]:
            for j in range(W):
                if w[j]:
                    print(a[i][j], end='')
            print()
    return

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    B = []
    for i in range(H):
        if '#' in A[i]:
            B.append(A[i])
    C = []
    for j in range(W):
        if '#' in [A[i][j] for i in range(H)]:
            C.append(j)
    for i in range(len(B)):
        print(''.join([B[i][j] for j in C]))
    return

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    h = [i for i in range(H) if '#' in A[i]]
    w = [j for j in range(W) if '#' in [A[i][j] for i in range(H)]]
    for i in h:
        print(''.join(A[i][j] for j in w))

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    A = list(map(list, zip(*A)))
    A = [a for a in A if '#' in a]
    A = list(map(list, zip(*A)))
    for a in A:
        print(''.join(a))

main()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    b = [[a[i][j] for i in range(H)] for j in range(W)]
    a = ["".join(i) for i in a if i.count("#") > 0]
    b = ["".join(i) for i in b if i.count("#") > 0]
    for i in a:
        print(i)
    for i in b:
        print(i)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = [list(a[i]) for i in range(H)]
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                b[i][j] = 1
            else:
                b[i][j] = 0
    c = [0] * W
    d = [0] * H
    for i in range(H):
        if sum(b[i]) == 0:
            d[i] = 1
    for j in range(W):
        for i in range(H):
            if a[i][j] == '#':
                c[j] = 1
    for i in range(H):
        if d[i] == 0:
            for j in range(W):
                if c[j] == 1:
                    print(a[i][j], end='')
            print()

=======
Suggestion 8

def main():
    H,W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    Hs = [0]*H
    Ws = [0]*W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                Hs[i] = 1
                Ws[j] = 1
    for i in range(H):
        if Hs[i] == 1:
            for j in range(W):
                if Ws[j] == 1:
                    print(grid[i][j], end = '')
            print()

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    B = list(zip(*A))
    C = ["".join(i) for i in B]
    i = 0
    j = 0
    while True:
        if i == H:
            break
        if "#" not in A[i]:
            del A[i]
            H -= 1
            continue
        i += 1
    while True:
        if j == W:
            break
        if "#" not in C[j]:
            for k in range(H):
                A[k] = A[k][:j] + A[k][j+1:]
            W -= 1
            continue
        j += 1
    for i in range(H):
        print(A[i])

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # ひとまず、#がある行と列を抽出
    rows = []
    cols = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                rows.append(i)
                cols.append(j)
    # 重複を除く
    rows = list(set(rows))
    cols = list(set(cols))
    # print(rows)
    # print(cols)

    # 抽出した行と列を使って、新しい行列を作成
    for i in range(len(rows)):
        for j in range(len(cols)):
            print(S[rows[i]][cols[j]], end="")
        print("")
