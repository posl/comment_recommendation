def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M, M, -1):
        for j in range(M, -1, -1):
            B[j] = C[i - j] - sum([A[k] * B[j - k] for k in range(1, j + 1)])
        A = B[:]
    print(*B)

if __name__ == '__main__':
    main()