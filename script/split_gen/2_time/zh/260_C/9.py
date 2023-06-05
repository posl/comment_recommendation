def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([i+1, A[i], B[i], A[i]+B[i]])
    C.sort(key=lambda x: x[3], reverse=True)
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    D = []
    for i in range(X):
        D.append(C[i][0])
    for i in range(X, X+Y):
        if C[i][1] == C[X-1][1]:
            D.append(C[i][0])
    for i in range(X+Y, X+Y+Z):
        if C[i][1] == C[X+Y-1][1] and C[i][2] == C[X+Y-1][2]:
            D.append(C[i][0])
    D.sort()
    for i in D:
        print(i)
