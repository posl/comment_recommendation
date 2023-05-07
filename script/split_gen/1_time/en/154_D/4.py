def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = 0
    for i in range(K):
        s += p[i]
    m = s
    for i in range(K, N):
        s += p[i] - p[i - K]
        m = max(m, s)
    print(m / 2 + K / 2)
main()
