def main():
    N = int(input())
    X = [0] * 5
    for i in range(N):
        T, X, A = map(int, input().split())
        X[T] += A
    for i in range(1, 5):
        X[i] += X[i - 1]
    print(max(X))

if __name__ == '__main__':
    main()