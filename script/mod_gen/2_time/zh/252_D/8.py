def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) * (d[i] - 2) // 6
    for i in range(n):
        ans += (d[a[i]] - 1) * (d[a[i]] - 2) // 2
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                continue
            ans += (d[a[i]] - 1) * (d[a[j]] - 1)
    print(ans)

if __name__ == '__main__':
    main()