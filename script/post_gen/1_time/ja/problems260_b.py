Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A_sorted = sorted(A, reverse=True)
    B_sorted = sorted(B, reverse=True)
    C_sorted = sorted(C, reverse=True)
    A_pass = A_sorted[:X]
    B_pass = []
    for b in B_sorted:
        if len(B_pass) == Y:
            break
        if b not in A_pass:
            B_pass.append(b)
    C_pass = []
    for c in C_sorted:
        if len(C_pass) == Z:
            break
        if c not in A_pass and c not in B_pass:
            C_pass.append(c)
    pass_list = A_pass + B_pass + C_pass
    pass_list_sorted = sorted(pass_list, reverse=True)
    for p in pass_list_sorted:
        print(A.index(p) + 1)

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = [i + 1 for i in range(N)]
    E = sorted(zip(A, D), reverse=True)
    F = sorted(zip(B, D), reverse=True)
    G = sorted(zip(C, D), reverse=True)
    H = []
    for i in range(X):
        H.append(E[i][1])
    for i in range(Y):
        if F[i][1] not in H:
            H.append(F[i][1])
    for i in range(Z):
        if G[i][1] not in H:
            H.append(G[i][1])
    H.sort()
    for i in range(X + Y + Z):
        print(H[i])

=======
Suggestion 3

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A = sorted([(A[i], i + 1) for i in range(N)], reverse=True)
    B = sorted([(B[i], i + 1) for i in range(N)], reverse=True)
    C = sorted([(C[i], i + 1) for i in range(N)], reverse=True)
    a, b, c = 0, 0, 0
    ans = set()
    while len(ans) < X:
        ans.add(A[a][1])
        a += 1
    while len(ans) < X + Y:
        ans.add(B[b][1])
        b += 1
    while len(ans) < X + Y + Z:
        ans.add(C[c][1])
        c += 1
    for i in sorted(list(ans)):
        print(i)

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    A = A[:X]
    B = B[:Y]
    C = C[:Z]
    for i in range(N):
        if A.count(A[i]) > 1:
            A.remove(A[i])
        if B.count(B[i]) > 1:
            B.remove(B[i])
        if C.count(C[i]) > 1:
            C.remove(C[i])
    A = set(A)
    B = set(B)
    C = set(C)
    for i in range(N):
        if A & B & C:
            print(i+1)
            A.remove(A[i])
            B.remove(B[i])
            C.remove(C[i])
        elif A & B:
            print(i+1)
            A.remove(A[i])
            B.remove(B[i])
        elif A & C:
            print(i+1)
            A.remove(A[i])
            C.remove(C[i])
        elif B & C:
            print(i+1)
            B.remove(B[i])
            C.remove(C[i])
        elif A:
            print(i+1)
            A.remove(A[i])
        elif B:
            print(i+1)
            B.remove(B[i])
        elif C:
            print(i+1)
            C.remove(C[i])
        else:
            break

=======
Suggestion 5

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    #print(A)
    #print(B)
    #print(C)
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(B)
    #print(C)
    for i in range(X):
        print(A.index(A[i])+1)
    for i in range(Y):
        print(B.index(B[i])+1)
    for i in range(Z):
        print(C.index(C[i])+1)

=======
Suggestion 6

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [A[i]+B[i] for i in range(N)]
    D = [i+1 for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    D.sort(reverse=True)
    a = 0
    b = 0
    c = 0
    d = 0
    while a < X:
        print(D[A.index(A[a])])
        A[a] = -1
        a += 1
    while b < Y:
        print(D[B.index(B[b])])
        B[b] = -1
        b += 1
    while c < Z:
        print(D[C.index(C[c])])
        C[c] = -1
        c += 1
    while d < N:
        if A[d] != -1:
            print(D[A.index(A[d])])
            A[d] = -1
        d += 1

=======
Suggestion 7

def main():
    # N, X, Y, Z = map(int, input().split())
    # A = list(map(int, input().split()))
    # B = list(map(int, input().split()))
    N, X, Y, Z = 15, 4, 3, 2
    A = [30, 65, 20, 95, 100, 45, 70, 85, 20, 35, 95, 50, 40, 15, 85]
    B = [0, 25, 45, 35, 65, 70, 80, 90, 40, 55, 20, 20, 45, 75, 100]
    # N, X, Y, Z = 5, 2, 1, 2
    # A = [0, 100, 0, 100, 0]
    # B = [0, 0, 100, 100, 0]
    # N, X, Y, Z = 6, 1, 0, 2
    # A = [80, 60, 80, 60, 70, 70]
    # B = [40, 20, 50, 90, 90, 80]
    # N, X, Y, Z = 15, 4, 3, 2
    # A = [30, 65, 20, 95, 100, 45, 70, 85, 20, 35, 95, 50, 40, 15, 85]
    # B = [0, 25, 45, 35, 65, 70, 80, 90, 40, 55, 20, 20, 45, 75, 100]
    # N, X, Y, Z = 5, 2, 1, 2
    # A = [0, 100, 0, 100, 0]
    # B = [0, 0, 100, 100, 0]
    # N, X, Y, Z = 6, 1, 0, 2
    # A = [80, 60, 80

=======
Suggestion 8

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda a, b: a + b, A, B))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    for i in range(1, N):
        if A[i] == A[i - 1]:
            A[i] = -1
        if B[i] == B[i - 1]:
            B[i] = -1
        if C[i] == C[i - 1]:
            C[i] = -1
    A = list(filter(lambda x: x != -1, A))
    B = list(filter(lambda x: x != -1, B))
    C = list(filter(lambda x: x != -1, C))
    ans = []
    for i in range(X):
        ans.append(A[i])
    for i in range(Y):
        ans.append(B[i])
    for i in range(Z):
        ans.append(C[i])
    ans.sort(reverse=True)
    for i in range(N):
        if A[i] in ans:
            print(i + 1)

=======
Suggestion 9

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #数学の点が高い方から X 人を合格とする。
    A1 = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
    A1 = [i[0] for i in A1[:X]]

    #次に、この時点でまだ合格となっていない受験者のうち、英語の点が高い方から Y 人を合格とする。
    B1 = sorted(enumerate(B), key=lambda x: x[1], reverse=True)
    B1 = [i[0] for i in B1[:Y]]

    #次に、この時点でまだ合格となっていない受験者のうち、数学と英語の合計点が高い方から Z 人を合格とする。
    C = [a+b for a, b in zip(A, B)]
    C1 = sorted(enumerate(C), key=lambda x: x[1], reverse=True)
    C1 = [i[0] for i in C1[:Z]]

    #A1, B1, C1の合計を取る
    D = A1 + B1 + C1
    D = sorted(set(D))

    #出力
    for i in D:
        print(i+1)

=======
Suggestion 10

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [a for a, b in sorted(zip(A, B), reverse=True)]
    B = [b for a, b in sorted(zip(A, B), reverse=True)]
    C = [a + b for a, b in zip(A, B)]
    C = [c for c, a, b in sorted(zip(C, A, B), reverse=True)]
    for i in range(N):
        if i < X:
            print(i + 1)
        elif i >= X and i < X + Y:
            if B[i] > C[X - 1]:
                print(i + 1)
        elif i >= X + Y:
            if A[i] + B[i] > C[X + Y - 1]:
                print(i + 1)
