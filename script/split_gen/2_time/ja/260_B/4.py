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
