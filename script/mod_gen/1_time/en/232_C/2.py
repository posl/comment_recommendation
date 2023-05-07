def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(M):
        A[i] -= 1
        B[i] -= 1
        C[i] -= 1
        D[i] -= 1
    for i in range(M):
        for j in range(M):
            if A[i] == A[j] and B[i] == B[j]:
                if C[i] != C[j] or D[i] != D[j]:
                    print("No")
                    return
            elif A[i] == B[j] and B[i] == A[j]:
                if C[i] != D[j] or D[i] != C[j]:
                    print("No")
                    return
            elif A[i] == C[j] and B[i] == D[j]:
                if C[i] != A[j] or D[i] != B[j]:
                    print("No")
                    return
            elif A[i] == D[j] and B[i] == C[j]:
                if C[i] != B[j] or D[i] != A[j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()