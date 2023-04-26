Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    p = [i for i in range(1, N + 1)]
    for i in range(M):
        for j in range(M):
            if AB[i] == CD[j]:
                p[AB[i][0] - 1], p[AB[i][1] - 1] = p[AB[i][1] - 1], p[AB[i][0] - 1]
    if p == [i for i in range(1, N + 1)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    P = list(range(1, N + 1))
    for p in permutations(P):
        if all(AB[i][0] == CD[p[AB[i][0] - 1] - 1][0] and AB[i][1] == CD[p[AB[i][1] - 1] - 1][1] for i in range(M)):
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    flag = 0
                    for m in range(M):
                        if (A[m] == i + 1 and B[m] == j + 1 and C[m] == k + 1 and D[m] == l + 1) or (A[m] == j + 1 and B[m] == i + 1 and C[m] == l + 1 and D[m] == k + 1):
                            flag = 1
                    if flag == 0:
                        print('No')
                        return
    print('Yes')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                print("Yes")
                return

    print("No")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    
    # 1, 2, ..., N の順列を作る
    p = list(range(1, N + 1))
    
    # 順列をひとつずつ調べる
    while True:
        # 順列 p で、A と C が同じ形になっているかを調べる
        ok = True
        for i in range(M):
            # A[i] と B[i] がひもで繋がれているか
            if p[A[i] - 1] == B[i]:
                # C[i] と D[i] がひもで繋がれているか
                if p[C[i] - 1] != D[i]:
                    ok = False
                    break
            # B[i] と A[i] がひもで繋がれているか
            if p[B[i] - 1] == A[i]:
                # D[i] と C[i] がひもで繋がれているか
                if p[D[i] - 1] != C[i]:
                    ok = False
                    break
        # 同じ形になっているなら Yes を出力して終了
        if ok:
            print('Yes')
            return
        
        # 次の順列を作る
        i = N - 1
        while i > 0 and p[i - 1] >= p[i]:
            i -= 1
        if i <= 0:
            break
        j = N - 1
        while p[j] <= p[i - 1]:
            j -= 1
        p[i - 1], p[j] = p[j], p

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        if C[i] > D[i]:
            C[i], D[i] = D[i], C[i]
    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                break
        else:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a - 1)
        B.append(b - 1)
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c - 1)
        D.append(d - 1)
    for p in itertools.permutations(range(N)):
        ok = True
        for i in range(M):
            if (p[A[i]] < p[B[i]]) != (C[i] < D[i]):
                ok = False
        if ok:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = []
    CD = []
    for i in range(M):
        a, b = map(int, input().split())
        AB.append((a, b))
    for i in range(M):
        c, d = map(int, input().split())
        CD.append((c, d))

    AB.sort()
    CD.sort()
    AB = tuple(AB)
    CD = tuple(CD)

    if AB == CD:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    # 2人のおもちゃの情報を取得
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(m):
        c_i, d_i = map(int, input().split())
        c.append(c_i)
        d.append(d_i)
    # 2人のおもちゃが同じ形であるかどうかを判定
    # 2人のおもちゃが同じ形であるとは、以下の条件を満たす数列 P が存在することをいいます。
    # P は (1, ..., N) を並べ替えて得られる。
    # 任意の 1 以上 N 以下の整数 i, j に対し、以下が成り立つ。
    # 高橋君のおもちゃにおいてボール i, j がひもで繋がれていることと、青木君のおもちゃにおいてボール P_i, P_j がひもで繋がれていることは同値である。
    # 高橋君のおもちゃのボールの組み合わせを列挙
    ab = []
    for i in range(m):
        ab.append((a[i], b[i]))
    # 青木君のおもちゃのボールの組み合わせを列挙
    cd = []
    for i in range(m):
        cd.append((c[i], d[i]))
    # 高橋君のおもちゃのボールの組み合わせを列挙
    ab = []
    for i in range(m):
        ab.append((a[i], b[i]))
    # 青木君のおもちゃの
