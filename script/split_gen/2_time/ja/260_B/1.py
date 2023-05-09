def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A = [(i+1, A[i]) for i in range(N)]
    B = [(i+1, B[i]) for i in range(N)]
    C = [(i+1, C[i]) for i in range(N)]
    A.sort(key=lambda x: x[1], reverse=True)
    B.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    A = [i[0] for i in A]
    B = [i[0] for i in B]
    C = [i[0] for i in C]
    ans = []
    for i in range(X):
        ans.append(A[i])
    for i in range(Y):
        if B[i] not in ans:
            ans.append(B[i])
    for i in range(Z):
        if C[i] not in ans:
            ans.append(C[i])
    ans.sort()
    for i in ans:
        print(i)
