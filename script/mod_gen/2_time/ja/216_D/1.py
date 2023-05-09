def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    K = [A[i][0] for i in range(M)]
    B = [A[i][1:] for i in range(M)]
    #print(N, M, A, K, B)
    C = [0] * N
    for i in range(M):
        for j in range(K[i]):
            C[B[i][j] - 1] += 1
    #print(C)
    for i in range(N):
        if C[i] % 2 != 0:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()