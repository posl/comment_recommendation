def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    X = ""
    for s in S:
        X += s
        X += "_"
    X = X[:-1]
    if len(X) < 3 or 16 < len(X):
        print(-1)
        return
    for t in T:
        if X == t:
            print(-1)
            return
    print(X)

if __name__ == '__main__':
    main()