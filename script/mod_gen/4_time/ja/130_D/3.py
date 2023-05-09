def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    total = 0
    r = 0
    for l in range(n):
        while r < n and total < k:
            total += a[r]
            r += 1
        if total < k:
            break
        ans += n - r + 1
        if l == r:
            r += 1
        else:
            total -= a[l]
    print(ans)

if __name__ == '__main__':
    main()