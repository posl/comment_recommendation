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
        d[a[i]] -= 1
        for j in range(1, 200001):
            if a[i] % j == 0 and (a[i] // j) in d:
                ans += d[a[i] // j]
    print(ans)

if __name__ == '__main__':
    main()