def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x % m for x in a]
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = (s[i] + a[i]) % m
    from collections import Counter
    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()