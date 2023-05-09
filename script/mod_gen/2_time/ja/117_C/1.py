def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    L = []
    for i in range(1, M):
        L.append(X[i] - X[i - 1])
    L.sort()
    print(sum(L[:M - N]))

if __name__ == '__main__':
    main()