def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:K])
    m = s
    for i in range(K, N):
        s += p[i] - p[i-K]
        if s > m:
            m = s
    print((m + K) / 2)
