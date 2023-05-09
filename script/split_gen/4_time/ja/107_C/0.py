def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        l = X[i]
        r = X[i+K-1]
        if l*r <= 0:
            ans = min(ans, min(abs(l), abs(r))*2 + max(abs(l), abs(r)))
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)
