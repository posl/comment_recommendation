def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        r = X[i+K-1]
        l = X[i]
        ans = min(ans, r-l+min(abs(r), abs(l)))
    print(ans)

if __name__ == '__main__':
    main()