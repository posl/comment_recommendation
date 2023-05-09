def main():
    n, k = map(int, input().split())
    s = input()
    c = 0
    l = 0
    r = 0
    ans = 0
    while r < n:
        if s[r] == '0':
            c += 1
        while c > k:
            if s[l] == '0':
                c -= 1
            l += 1
        ans = max(ans, r-l+1)
        r += 1
    print(ans)
