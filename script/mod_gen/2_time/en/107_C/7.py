def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**10
    for i in range(N-K+1):
        if X[i] < 0:
            if X[i+K-1] < 0:
                ans = min(ans, abs(X[i+K-1]))
            else:
                ans = min(ans, abs(X[i+K-1]) + abs(X[i]))
        else:
            ans = min(ans, abs(X[i]))
    print(ans)

if __name__ == '__main__':
    main()