def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    m = s
    for i in range(n - k):
        s -= p[i]
        s += p[i + k]
        m = max(m, s)
    print((m + k) / 2)
main()

if __name__ == '__main__':
    main()