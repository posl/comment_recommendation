def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        a[i] %= 200
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for key in d:
        ans += d[key] * (d[key] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()