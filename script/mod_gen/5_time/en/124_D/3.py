def main():
    n,k = map(int,input().split())
    s = input()
    l = 0
    r = 0
    ans = 0
    while r < n:
        while r < n and s[r] == '1':
            r += 1
        ans = max(ans,r-l)
        r += 1
        while r < n and s[r] == '0':
            r += 1
        while k > 0 and l < r:
            k -= 1
            l += 1
            while l < r and s[l] == '1':
                l += 1
    print(ans)

if __name__ == '__main__':
    main()