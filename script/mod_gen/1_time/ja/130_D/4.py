def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    l = 0
    r = 0
    sum = 0
    while l < n:
        if r == n:
            sum -= a[l]
            l += 1
        elif sum < k:
            sum += a[r]
            r += 1
        else:
            sum -= a[l]
            l += 1
        if sum >= k:
            ans += n - r + 1
    print(ans)

if __name__ == '__main__':
    main()