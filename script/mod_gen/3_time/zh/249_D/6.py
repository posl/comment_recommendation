def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for i in range(n):
        c[a[i]] = c.get(a[i], 0) + 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i] == 0:
                continue
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if c.get(a[i] // a[j], 0) == 0:
                continue
            ans += c[a[i] // a[j]]
    print(ans)

if __name__ == '__main__':
    main()