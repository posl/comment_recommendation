def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    m = s
    for i in range(n - k):
        s = s - p[i] + p[i + k]
        if s > m:
            m = s
    print((m + k) / 2)
main()
