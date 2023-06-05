def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        d[c[i]] = 1
    ans = len(d)
    for i in range(n-k):
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        if c[i+k] in d:
            d[c[i+k]] += 1
        else:
            d[c[i+k]] = 1
        ans = max(ans, len(d))
    print(ans)

if __name__ == '__main__':
    main()