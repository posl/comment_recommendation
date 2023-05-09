def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    l = 0
    r = 0
    while r < n:
        while r < n and s[r] == "X":
            r += 1
        ans = max(ans, r - l)
        if r == n:
            break
        l = r
        while r < n and r - l < k and s[r] == ".":
            r += 1
        if r == n:
            break
        if s[r] == "X":
            r += 1
        l = r
    print(ans)

if __name__ == '__main__':
    main()