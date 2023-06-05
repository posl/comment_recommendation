def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        l = X[i]
        r = X[i+K-1]
        ans = min(ans, min(abs(l)+abs(l-r), abs(r)+abs(l-r)))
    print(ans)

if __name__ == '__main__':
    main()