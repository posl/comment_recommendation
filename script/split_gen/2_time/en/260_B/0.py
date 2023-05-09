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
