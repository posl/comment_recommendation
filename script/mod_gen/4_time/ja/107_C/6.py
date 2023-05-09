def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        if X[i] <= 0 and X[i+K-1] <= 0:
            ans = min(ans, abs(X[i]))
        elif X[i] <= 0 and X[i+K-1] >= 0:
            ans = min(ans, 2*abs(X[i])+X[i+K-1])
        elif X[i] >= 0 and X[i+K-1] >= 0:
            ans = min(ans, abs(X[i+K-1]))
    print(ans)

if __name__ == '__main__':
    solve()