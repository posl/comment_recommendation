def main():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    d = {}
    for i in range(K):
        if c[i] not in d:
            d[c[i]] = 0
        d[c[i]] += 1
        ans = max(ans,len(d))
    for i in range(K,N):
        d[c[i-K]] -= 1
        if d[c[i-K]] == 0:
            del d[c[i-K]]
        if c[i] not in d:
            d[c[i]] = 0
        d[c[i]] += 1
        ans = max(ans,len(d))
    print(ans)

if __name__ == '__main__':
    main()