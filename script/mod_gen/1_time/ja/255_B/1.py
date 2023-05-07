def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    print(solve(N, K, A, X, Y))

if __name__ == '__main__':
    main()