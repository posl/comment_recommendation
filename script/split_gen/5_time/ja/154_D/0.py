def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    total = sum(p[0:K])
    max_total = total
    for i in range(N-K):
        total = total - p[i] + p[i+K]
        if total > max_total:
            max_total = total
    print((max_total + K)/2)
main()
