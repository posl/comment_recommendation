def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        a[i] = a[i] - k
    s = 0
    ans = 0
    for i in range(n):
        s += a[i]
        if s == 0:
            ans += 1
        if s in d:
            ans += d[s]
            d[s] += 1
        else:
            d[s] = 1
    print(ans)

if __name__ == '__main__':
    main()