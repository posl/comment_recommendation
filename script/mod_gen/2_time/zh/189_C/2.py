def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        l = i
        r = i
        x = a[i]
        while l > 0 and a[l-1] >= x:
            l -= 1
        while r < n-1 and a[r+1] >= x:
            r += 1
        ans = max(ans, x*(r-l+1))
    print(ans)

if __name__ == '__main__':
    main()