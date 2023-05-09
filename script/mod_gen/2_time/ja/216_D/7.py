def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    A = [[A[i][j] for j in range(1, A[i][0] + 1)] for i in range(M)]
    B = [0 for _ in range(N + 1)]
    for i in range(M):
        for j in range(len(A[i])):
            B[A[i][j]] += 1
    for i in range(1, N + 1):
        if B[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()