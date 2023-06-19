def solve():
    s = input()
    k = int(input())
    n = len(s)
    if n == 1:
        print(1)
        return
    if s[0] == s[-1] and s[0] == 'X':
        r = 0
        for i in range(n):
            if s[i] == 'X':
                r += 1
            else:
                break
        l = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'X':
                l += 1
            else:
                break
        print(min(n, r+l+k*2))
    else:
        r = 0
        for i in range(n):
            if s[i] == 'X':
                r += 1
            else:
                break
        l = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'X':
                l += 1
            else:
                break
        print(min(n, r+l+k*2-1))
solve()
