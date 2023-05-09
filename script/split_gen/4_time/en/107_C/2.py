def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, min(abs(X[i+K-1]-X[i])+abs(X[i]), abs(X[i+K-1]-X[i])+abs(X[i+K-1])))
    print(ans)
