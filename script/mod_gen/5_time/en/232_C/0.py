def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    if M == 0:
        print("Yes")
        return
    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                A[i] = 0
                B[i] = 0
                C[j] = 0
                D[j] = 0
    if 0 in A:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()