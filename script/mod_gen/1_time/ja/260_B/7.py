def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda a, b: a + b, A, B))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    for i in range(1, N):
        if A[i] == A[i - 1]:
            A[i] = -1
        if B[i] == B[i - 1]:
            B[i] = -1
        if C[i] == C[i - 1]:
            C[i] = -1
    A = list(filter(lambda x: x != -1, A))
    B = list(filter(lambda x: x != -1, B))
    C = list(filter(lambda x: x != -1, C))
    ans = []
    for i in range(X):
        ans.append(A[i])
    for i in range(Y):
        ans.append(B[i])
    for i in range(Z):
        ans.append(C[i])
    ans.sort(reverse=True)
    for i in range(N):
        if A[i] in ans:
            print(i + 1)

if __name__ == '__main__':
    main()