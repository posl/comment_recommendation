def main():
    n = int(input())
    a = [int(x) % 200 for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()