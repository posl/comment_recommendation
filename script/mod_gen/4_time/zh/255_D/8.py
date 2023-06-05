def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    print(N, Q, A, X)
    for i in range(Q):
        print(X[i])

if __name__ == '__main__':
    main()