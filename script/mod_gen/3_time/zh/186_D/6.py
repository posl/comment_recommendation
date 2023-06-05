def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = 0
    r = n - 1
    ans = 0
    while l < r:
        ans += a[r] - a[l]
        r -= 1
        if l < r:
            ans += a[r] - a[l]
            l += 1
    print(ans)

if __name__ == '__main__':
    main()