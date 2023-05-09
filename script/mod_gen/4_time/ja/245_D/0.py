def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M):
        for j in range(min(N, i + 1)):
            B[i - j] -= A[j] * C[i]
    print(*B)

if __name__ == '__main__':
    main()