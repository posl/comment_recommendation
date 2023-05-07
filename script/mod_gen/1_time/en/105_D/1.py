def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    d = {}
    for i in range(n+1):
        r = s[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for v in d.values():
        ans += v * (v-1) // 2
    print(ans)
main()

if __name__ == '__main__':
    main()