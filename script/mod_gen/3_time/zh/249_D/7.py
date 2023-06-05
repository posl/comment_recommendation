def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    d = {}
    for i in range(1, n+1):
        if a[i] not in d.keys():
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] not in d.keys():
                continue
            ans += d[a[i] // a[j]]
    print(ans)

if __name__ == '__main__':
    main()