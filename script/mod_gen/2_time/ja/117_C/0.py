def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = []
    for i in range(M - 1):
        D.append(X[i + 1] - X[i])
    D.sort()
    ans = 0
    for i in range(M - N):
        ans += D[i]
    print(ans)

if __name__ == '__main__':
    main()