def solve(s):
    n = len(s)
    mod = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
        else:
            ans = (ans*3 + c)%mod
            ans = (ans*3 + b)%mod
            ans = (ans*3 + a)%mod
            a = (a*3)%mod
            b = (b*3)%mod
            c = (c*3)%mod
    return ans

if __name__ == '__main__':
    solve()