def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    d = {}
    for i in range(n + 1):
        if s[i] - k in d:
            ans += d[s[i] - k]
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    print(ans)

if __name__ == '__main__':
    main()