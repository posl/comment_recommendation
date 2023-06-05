def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    for i in range(n):
        print(ans - d[a[i]] + 1)

if __name__ == '__main__':
    main()