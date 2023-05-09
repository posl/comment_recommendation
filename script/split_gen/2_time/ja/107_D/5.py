def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = []
    for i in range(N):
        C.append(B.index(A[i]))
    D = []
    for i in range(N):
        D.append(C[i] - i)
    E = sorted(D)
    F = []
    for i in range(N):
        F.append(E.index(D[i]))
    G = []
    for i in range(N):
        G.append(B[F[i]])
    print(G[N//2])
