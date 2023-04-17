Synthesizing 10/10 solutions

=======

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H

=======

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    B = list(zip(*A))
    C = []
    D = []
    for i in range(H):
        if '#' in A[i]:
            C.append(A[i])
    for j in range(W):
        if '#' in B[j]:
            D.append(B[j])
    E = list(zip(*D))
    for i in range(len(C)):
        print(''.join(C[i]))
    for j in range(len(E)):
        print(''.join(E[j]))

=======

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    while True:
        cnt = 0
        for i in range(h):
            if all(a[i][j] == '.' for j in range(w)):
                a.pop(i)
                h -= 1
                cnt += 1
                break
        if cnt == 0:
            break
    while True:
        cnt = 0
        for j in range(w):
            if all(a[i][j] == '.' for i in range(h)):
                for i in range(h):
                    a[i].pop(j)
                w -= 1
                cnt += 1
                break
        if cnt == 0:
            break
    for i in range(h):
        print(''.join(a[i]))

=======

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    b = []
    for i in range(h):
        if '#' in a[i]:
            b.append(i)
    c = []
    for i in range(w):
        if '#' in [a[j][i] for j in range(h)]:
            c.append(i)

    for i in b:
        print(''.join([a[i][j] for j in c]))

=======

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    for _ in range(H):
        if all(A[_].count('#') == W for _ in range(H)):
            A.pop(_)
            break
    for _ in range(W):
        if all(A[i][_] == '#' for i in range(len(A))):
            for i in range(len(A)):
                A[i].pop(_)
            break
    for _ in A:
        print(''.join(_))

=======

def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(input())

    # 行の削除
    for i in range(H):
        if all(A[i][j] == '.' for j in range(W)):
            A[i] = None

    # 列の削除
    for j in range(W):
        if all(A[i][j] == '.' for i in range(H)):
            for i in range(H):
                A[i] = A[i][:j] + A[i][j+1:]

    # 行の出力
    for i in range(H):
        if A[i] is not None:
            print(A[i])

=======

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]

    while True:
        # 横方向の白マスのみからなる行を削除
        for i in range(H):
            if a[i] == ['.'] * W:
                a.pop(i)
                H -= 1
                break
        else:
            break

    while True:
        # 縦方向の白マスのみからなる列を削除
        for j in range(W):
            if all([a[i][j] == '.' for i in range(H)]):
                for i in range(H):
                    a[i].pop(j)
                W -= 1
                break
        else:
            break

    for i in range(len(a)):
        print(''.join(a[i]))

main()

=======

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    #print(H, W)
    #print(a)
    #print("")

    b = []
    for i in range(H):
        if "#" in a[i]:
            b.append(a[i])
    #print(b)
    #print("")

    c = []
    for i in range(W):
        if "#" in [b[j][i] for j in range(len(b))]:
            c.append([b[j][i] for j in range(len(b))])
    #print(c)
    #print("")

    for i in range(len(c[0])):
        print("".join([c[j][i] for j in range(len(c))]))

=======

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 一列ごとに黒いマスがあるかどうかを確認
    # あればTrue, なければFalse
    col = [False for _ in range(W)]
    for i in range(W):
        for j in range(H):
            if S[j][i] == '#':
                col[i] = True
                break

    # 一行ごとに黒いマスがあるかどうかを確認
    # あればTrue, なければFalse
    row = [False for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                row[i] = True
                break

    # 一列一行ともに黒いマスがなければ出力しない
    for i in range(H):
        if row[i]:
            for j in range(W):
                if col[j]:
                    print(S[i][j], end='')
            print()

=======

def read():
    return map(int, input().split())
