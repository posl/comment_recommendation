def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    d = []
    for i in range(M-1):
        d.append(X[i+1] - X[i])
    d.sort()
    print(sum(d[:M-N]))

if __name__ == '__main__':
    main()