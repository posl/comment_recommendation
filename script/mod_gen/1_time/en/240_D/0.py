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
        if a[i] in d:
            ans += 1
            if d[a[i]] == 1:
                del d[a[i]]
            else:
                d[a[i]] -= 1
    print(ans)

if __name__ == '__main__':
    main()