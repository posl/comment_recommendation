def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        X[i] = (A[i - 1] - A[i]) // 2
    for i in range(N):
        X[i] += X[i - 1]
    for i in range(N):
        X[i] += A[i]
    print(*X)

if __name__ == '__main__':
    main()