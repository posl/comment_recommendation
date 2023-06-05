def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    if K == 1:
        print(0)
        return
    if K == N:
        print(X[-1] - X[0])
        return
    ans = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        ans = min(ans, min(abs(left), abs(right)) + right - left)
    print(ans)

if __name__ == '__main__':
    main()