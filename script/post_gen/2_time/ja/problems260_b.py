Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A = [(i, A[i]) for i in range(N)]
    B = [(i, B[i]) for i in range(N)]
    C = [(i, C[i]) for i in range(N)]
    A.sort(key=lambda x: x[1], reverse=True)
    B.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    A = [x[0] for x in A]
    B = [x[0] for x in B]
    C = [x[0] for x in C]
    for i in range(X):
        print(A[i] + 1)
    for i in range(Y):
        if B[i] not in A[:X]:
            print(B[i] + 1)
    for i in range(Z):
        if C[i] not in A[:X] and C[i] not in B[:Y]:
            print(C[i] + 1)

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A = [(i+1, A[i]) for i in range(N)]
    B = [(i+1, B[i]) for i in range(N)]
    C = [(i+1, C[i]) for i in range(N)]
    A.sort(key=lambda x: x[1], reverse=True)
    B.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    A = [i[0] for i in A]
    B = [i[0] for i in B]
    C = [i[0] for i in C]
    ans = []
    for i in range(X):
        ans.append(A[i])
    for i in range(Y):
        if B[i] not in ans:
            ans.append(B[i])
    for i in range(Z):
        if C[i] not in ans:
            ans.append(C[i])
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i], B[i], i+1])
    C.sort(reverse=True)
    for i in range(X):
        print(C[i][2])
    C = C[X:]
    C.sort(key=lambda x: x[1], reverse=True)
    for i in range(Y):
        print(C[i][2])
    C = C[Y:]
    C.sort(key=lambda x: x[0]+x[1], reverse=True)
    for i in range(Z):
        print(C[i][2])

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i]+B[i] for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    a = []
    b = []
    c = []
    for i in range(N):
        if A[i] in a:
            continue
        else:
            a.append(A[i])
            if len(a) == X:
                break
    for i in range(N):
        if B[i] in b:
            continue
        else:
            b.append(B[i])
            if len(b) == Y:
                break
    for i in range(N):
        if C[i] in c:
            continue
        else:
            c.append(C[i])
            if len(c) == Z:
                break
    for i in range(N):
        if A[i] in a and B[i] in b and C[i] in c:
            print(i+1)

=======
Suggestion 5

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    D = []
    E = []
    for i in range(N):
        C.append([A[i], B[i], i+1])
    C.sort(reverse=True)
    for i in range(X):
        D.append(C[i][2])
    for i in range(X, N):
        if C[i][1] not in D:
            D.append(C[i][1])
    for i in range(X+Y):
        E.append(C[i][2])
    for i in range(X+Y, N):
        if C[i][0]+C[i][1] not in E:
            E.append(C[i][0]+C[i][1])
    for i in range(X+Y+Z):
        if i+1 not in E:
            E.append(i+1)
    E.sort()
    for i in range(X+Y+Z):
        print(E[i])

=======
Suggestion 6

def main():
    # 入力
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 処理
    C = [A[i] + B[i] for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    A_pass = A[:X]
    B_pass = B[:Y]
    C_pass = C[:Z]
    A_pass.extend(B_pass)
    A_pass.extend(C_pass)
    A_pass = list(set(A_pass))
    A_pass.sort()
    # 出力
    for i in range(len(A_pass)):
        print(A_pass[i])

=======
Suggestion 7

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 1. 数学の点が高い方から X 人を合格とする。
    A.sort(reverse=True)
    X_list = A[:X]
    #print(X_list)

    # 2. 次に、この時点でまだ合格となっていない受験者のうち、英語の点が高い方から Y 人を合格とする。
    B.sort(reverse=True)
    Y_list = B[:Y]
    #print(Y_list)

    # 3. 次に、この時点でまだ合格となっていない受験者のうち、数学と英語の合計点が高い方から Z 人を合格とする。
    C = [(A[i] + B[i]) for i in range(N)]
    C.sort(reverse=True)
    Z_list = C[:Z]
    #print(Z_list)

    # 4. ここまでで合格となっていない受験者は、不合格とする。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。

=======
Suggestion 8

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_b = []
    for i in range(n):
        a_b.append([a[i], b[i], i + 1])
    a_b.sort(key=lambda x: x[0], reverse=True)
    a_b = a_b[:x]
    a_b.sort(key=lambda x: x[1], reverse=True)
    a_b = a_b[:y]
    a_b.sort(key=lambda x: x[0] + x[1], reverse=True)
    a_b = a_b[:z]
    a_b.sort(key=lambda x: x[2])
    for i in a_b:
        print(i[2])

=======
Suggestion 9

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A = [80, 60, 80, 60, 70, 70]
    # B = [40, 20, 50, 90, 90, 80]
    # N, X, Y, Z = 6, 1, 0, 2
    # A = [0, 100, 0, 100, 0]
    # B = [0, 0, 100, 100, 0]
    # N, X, Y, Z = 5, 2, 1, 2
    # A = [30, 65, 20, 95, 100, 45, 70, 85, 20, 35, 95, 50, 40, 15, 85]
    # B = [0, 25, 45, 35, 65, 70, 80, 90, 40, 55, 20, 20, 45, 75, 100]
    # N, X, Y, Z = 15, 4, 3, 2

    # A = [80, 60, 80, 60, 70, 70]
    # B = [40, 20, 50, 90, 90, 80]
    # N, X, Y, Z = 6, 1, 0, 2

    # A = [0, 100, 0, 100, 0]
    # B = [0, 0, 100, 100, 0]
    # N, X, Y, Z = 5, 2, 1, 2

    # A = [30, 65, 20, 95, 100, 45, 70, 85, 20, 35, 95, 50, 40, 15, 85]
    # B = [0, 25, 45, 35, 65, 70, 80, 90, 40, 55, 20, 20

=======
Suggestion 10

def main():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted([A[i],i+1] for i in range(N))
    B = sorted([B[i],i+1] for i in range(N))
    AB = sorted([[A[i][0]+B[i][0],A[i][1]] for i in range(N)])
    a = []
    for i in range(X):
        a.append(A.pop()[1])
    for i in range(Y):
        a.append(B.pop()[1])
    for i in range(Z):
        a.append(AB.pop()[1])
    a.sort()
    for i in a:
        print(i)
