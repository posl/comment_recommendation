def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    for i in range(n):
        print(ans - (d[a[i]] - 1))

if __name__ == '__main__':
    main()