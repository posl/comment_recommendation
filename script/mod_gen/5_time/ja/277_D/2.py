def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            if A[i] != B[len(B) - 1]:
                B.append(A[i])
    B.append(B[0] + M)
    #print(B)
    #print(len(B))
    C = []
    for i in range(len(B) - 1):
        C.append(B[i + 1] - B[i])
    #print(C)
    #print(len(C))
    D = []
    for i in range(len(C)):
        if i == 0:
            D.append(C[i] - 1)
        else:
            if C[i] - C[i - 1] < 0:
                D.append(C[i] - C[i - 1] + M)
            else:
                D.append(C[i] - C[i - 1])
    #print(D)
    #print(len(D))
    E = []
    for i in range(len(D)):
        if i == 0:
            E.append(D[i] // 2)
        else:
            if D[i] // 2 < 0:
                E.append(D[i] // 2 + M)
            else:
                E.append(D[i] // 2)
    #print(E)
    #print(len(E))
    F = []
    for i in range(len(E)):
        if i == 0:
            F.append(E[i] * (E[i] + 1) // 2)
        else:
            if E[i] * (E[i] + 1) // 2 < 0:
                F.append(E[i] * (E[i] + 1) // 2 + M * E[i])
            else:
                F.append(E[i] * (E[i] + 1) // 2)
    #print(F)
    #print(len(F))
    print(sum(F))

if __name__ == '__main__':
    main()