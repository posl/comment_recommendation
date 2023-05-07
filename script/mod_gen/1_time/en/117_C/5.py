def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    D = []
    for i in range(M-1):
        D.append(X[i+1] - X[i])
    D.sort()
    ans = sum(D[:M-N])
    print(ans)

if __name__ == '__main__':
    main()