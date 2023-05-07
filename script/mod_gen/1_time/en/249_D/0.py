def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i] == a[j]:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                ans += d[a[i] // a[j]]
    print(ans)

if __name__ == '__main__':
    main()