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
