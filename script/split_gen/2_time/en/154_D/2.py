def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:K])
    t = s
    for i in range(K, N):
        t = t - p[i-K] + p[i]
        s = max(s, t)
    print((s + K) / 2)
