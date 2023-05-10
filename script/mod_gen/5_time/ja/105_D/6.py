def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x % m for x in a]
    for i in range(n - 1):
        a[i + 1] += a[i]
        a[i + 1] %= m
    from collections import defaultdict
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    for x in a:
        ans += d[x]
        d[x] += 1
    print(ans)
main()

if __name__ == '__main__':
    main()