def  main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
    ans = len(d)
    for i in range(1, n-k+1):
        if d[c[i-1]] == 1:
            del d[c[i-1]]
        else:
            d[c[i-1]] -= 1
        if c[i+k-1] in d:
            d[c[i+k-1]] += 1
        else:
            d[c[i+k-1]] = 1
        ans = max(ans, len(d))
    print(ans)
