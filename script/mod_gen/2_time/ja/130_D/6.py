def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    r = 0
    ans = 0
    s = 0
    while l < n:
        while s < k and r < n:
            s += a[r]
            r += 1
        if s < k:
            break
        ans += n - r + 1
        s -= a[l]
        l += 1
    print(ans)

if __name__ == '__main__':
    main()