def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans += d[s % m]
        d[s % m] += 1
    print(ans)
main()

if __name__ == '__main__':
    main()