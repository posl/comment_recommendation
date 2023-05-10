def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    ans = len(d)
    for i in range(n-k):
        if d[c[i]] == 1:
            del d[c[i]]
        else:
            d[c[i]] -= 1
        if c[i+k] not in d:
            d[c[i+k]] = 1
        else:
            d[c[i+k]] += 1
        ans = max(ans,len(d))
    print(ans)
main()

if __name__ == '__main__':
    main()