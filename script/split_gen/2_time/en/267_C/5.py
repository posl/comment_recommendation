def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            B.append(B[i-1] + A[i])
    #print(B)
    C = []
    for i in range(N-M+1):
        if i == 0:
            C.append(B[i+M-1])
        else:
            C.append(B[i+M-1] - B[i-1])
    #print(C)
    D = []
    for i in range(N-M+1):
        if i == 0:
            D.append(i+1)
        else:
            D.append(D[i-1] + 1)
    #print(D)
    E = []
    for i in range(N-M+1):
        E.append(C[i] * D[i])
    #print(E)
    print(max(E))
