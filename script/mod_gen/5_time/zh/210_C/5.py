def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 0
        d[c[i]] += 1
    ans = len(d)
    for i in range(k, n):
        d[c[i]] = 1
        d[c[i-k]] -= 1
        if d[c[i-k]] == 0:
            del d[c[i-k]]
        ans = max(ans, len(d))
    print(ans)

if __name__ == '__main__':
    main()