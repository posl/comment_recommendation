def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(M):
        B.append(A[i][1:])
    C = []
    for i in range(M):
        for j in range(len(B[i])):
            C.append(B[i][j])
    D = set(C)
    if len(D) == N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()