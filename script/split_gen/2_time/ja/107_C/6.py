def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, X[i+K-1]-X[i]+min(abs(X[i]), abs(X[i+K-1])))
    print(ans)
