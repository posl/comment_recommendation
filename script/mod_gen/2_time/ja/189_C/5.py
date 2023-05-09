def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        cnt = 0
        while r < n:
            while r < n and a[r] >= x:
                r += 1
            cnt += max(0, r-l)
            while l < r and a[l] < x:
                l += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()