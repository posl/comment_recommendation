def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    K = min(K, N)
    ans = 0
    for i in range(K+1):
        for j in range(K+1-i):
            l = V[:i]
            r = V[N-j:]
            lr = sorted(l + r)
            m = K-i-j
            ans = max(ans, sum(lr[m:]))
    print(ans)
