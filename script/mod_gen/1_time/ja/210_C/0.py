def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    ans = len(d)
    for i in range(k, n):
        if d[c[i-k]] == 1:
            del d[c[i-k]]
        else:
            d[c[i-k]] -= 1
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
        ans = max(ans, len(d))
    print(ans)

if __name__ == '__main__':
    main()