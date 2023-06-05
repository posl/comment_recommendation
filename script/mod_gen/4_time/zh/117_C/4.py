def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    # print(X)
    if N >= M:
        print(0)
        return
    # print(X)
    # print(N, M)
    x = [0] * (M - 1)
    # print(x)
    for i in range(M - 1):
        x[i] = X[i + 1] - X[i]
    # print(x)
    x.sort(reverse=True)
    # print(x)
    print(sum(x[N - 1:]))

if __name__ == '__main__':
    main()