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
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()