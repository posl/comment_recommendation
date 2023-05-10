def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if X[i] < 0 and X[i+K-1] < 0:
            ans = min(ans, -X[i])
        elif X[i] < 0 and X[i+K-1] >= 0:
            ans = min(ans, -X[i]*2+X[i+K-1])
        elif X[i] >= 0 and X[i+K-1] >= 0:
            ans = min(ans, X[i+K-1])
    print(ans)

if __name__ == '__main__':
    main()