Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = [[A[i], i] for i in range(N)]
    E = [[B[i], i] for i in range(N)]
    F = [[C[i], i] for i in range(N)]
    D.sort(reverse=True)
    E.sort(reverse=True)
    F.sort(reverse=True)
    D = D[:X]
    E = E[:Y]
    F = F[:Z]
    G = D + E + F
    G.sort()
    for i in range(len(G)):
        print(G[i][1]+1)

main()

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i], B[i], A[i]+B[i], i+1])
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[0], reverse=True)
    for i in range(X):
        print(C[i][3])
    for i in range(X, X+Y):
        print(C[i][3])
    for i in range(X+Y, X+Y+Z):
        print(C[i][3])

=======
Suggestion 3

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = [[A[i], B[i], C[i], i + 1] for i in range(N)]
    D.sort(key=lambda x: (-x[0], x[3]))
    D.sort(key=lambda x: (-x[2], x[3]))
    D.sort(key=lambda x: (-x[1], x[3]))
    for i in range(X + Y + Z):
        print(D[i][3])

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append((A[i] + B[i], i + 1))
    C.sort(key=lambda x: -x[0])
    D = C[:X]
    C.sort(key=lambda x: -x[1])
    E = C[:Y]
    F = D + E
    F.sort(key=lambda x: -x[0])
    G = F[:Z]
    G.sort(key=lambda x: x[1])
    for i in range(Z):
        print(G[i][1])

=======
Suggestion 5

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], i + 1))
    c.sort(reverse = True)
    d = c[:x]
    c = c[x:]
    d.sort(key = lambda x: x[1], reverse = True)
    d += c[:y]
    c = c[y:]
    d.sort(key = lambda x: x[0] + x[1], reverse = True)
    d += c[:z]
    d.sort(key = lambda x: x[2])
    for i in d:
        print(i[2])

=======
Suggestion 6

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] + b[i] for i in range(n)]
    d = sorted(range(n), key=lambda i: a[i], reverse=True)
    e = sorted(range(n), key=lambda i: b[i], reverse=True)
    f = sorted(range(n), key=lambda i: c[i], reverse=True)
    g = []
    for i in range(x):
        g.append(d[i])
    for i in range(y):
        g.append(e[i])
    for i in range(z):
        g.append(f[i])
    h = sorted(list(set(g)))
    for i in h:
        print(i+1)

=======
Suggestion 7

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [(A[i] + B[i], A[i], B[i], i + 1) for i in range(N)]
    C.sort(reverse = True)
    for i in range(X + Y + Z):
        if i < X:
            print(C[i][3])
        elif i < X + Y:
            if C[i][1] < C[X - 1][1]:
                print(C[i][3])
        else:
            if C[i][1] < C[X - 1][1] and C[i][2] < C[X + Y - 1][2]:
                print(C[i][3])

=======
Suggestion 8

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted([(i, A[i], B[i], A[i] + B[i]) for i in range(N)], key=lambda x: (x[1], -x[0]), reverse=True)
    D = sorted([(i, A[i], B[i], A[i] + B[i]) for i in range(N)], key=lambda x: (x[2], -x[0]), reverse=True)
    E = sorted([(i, A[i], B[i], A[i] + B[i]) for i in range(N)], key=lambda x: (x[3], -x[0]), reverse=True)
    F = set()
    for i in range(X):
        F.add(C[i][0])
    for i in range(Y):
        F.add(D[i][0])
    for i in range(Z):
        F.add(E[i][0])
    for i in range(1, N + 1):
        if i in F:
            print(i)

=======
Suggestion 9

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 採用された人の番号
    admission = []

    # 1. 最高点数の人をX人採用
    # 2. 1で採用されなかった人の中で最高点数の人をY人採用
    # 3. 2で採用されなかった人の中で最高点数の人をZ人採用

    # 1. 最高点数の人をX人採用
    for i in range(X):
        # 最高点数の人の番号を探す
        max_point = max(A)
        max_index = A.index(max_point)
        # 採用された人の番号に追加
        admission.append(max_index + 1)
        # 採用された人の点数を-1にして採用されていることを示す
        A[max_index] = -1

    # 2. 1で採用されなかった人の中で最高点数の人をY人採用
    for i in range(Y):
        # 最高点数の人の番号を探す
        max_point = max(B)
        max_index = B.index(max_point)
        # 採用された人の番号に追加
        admission.append(max_index + 1)
        # 採用された人の点数を-1にして採用されていることを示す
        B[max_index] = -1

    # 3. 2で採用されなかった人の中で最高点数の人をZ人採用
    for i in range(Z):
        # 最高点数の人の番号を探す
        max_point = max(A, B)
        max_index = A.index(max_point)
        # 採用された人の番号に追加
        admission.append(max_index + 1)
        # 採用され

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
