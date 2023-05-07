def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append(A[i]+B[i])
    D = sorted(range(len(C)), key=C.__getitem__, reverse=True)
    E = sorted(D[:X])
    F = sorted(list(set(D)-set(E))[:Y])
    G = sorted(list(set(list(set(D)-set(E)))-set(F))[:Z])
    H = sorted(list(set(list(set(list(set(D)-set(E)))-set(F)))-set(G)))
    for i in range(len(E)):
        print(E[i]+1)
    for i in range(len(F)):
        print(F[i]+1)
    for i in range(len(G)):
        print(G[i]+1)
    for i in range(len(H)):
        print(H[i]+1)
