def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, abs(X[i]) + abs(X[i+K-1]-X[i]), abs(X[i+K-1]) + abs(X[i+K-1]-X[i]))
    print(ans)

if __name__ == '__main__':
    main()