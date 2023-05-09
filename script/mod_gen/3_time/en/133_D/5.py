def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    X = [0] * N
    X[0] = (S - N * A[0]) // 2
    for i in range(1, N):
        X[i] = A[i - 1] - X[i - 1]
    print(*X)

if __name__ == '__main__':
    main()