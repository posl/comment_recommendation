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
        if d[a[i]] > 0:
            ans += 1
            d[a[i]] -= 1
            if a[i] - 1 in d:
                d[a[i] - 1] += 1
            else:
                d[a[i] - 1] = 1
    print(ans)

if __name__ == '__main__':
    main()