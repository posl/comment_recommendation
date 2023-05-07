def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(n):
        while r < n and s + a[r] < k:
            s += a[r]
            r += 1
        if r == n:
            break
        ans += n - r
        s -= a[l]
    print(ans)

if __name__ == '__main__':
    main()