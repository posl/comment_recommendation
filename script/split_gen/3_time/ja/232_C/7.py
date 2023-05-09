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
