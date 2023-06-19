def solve():
    s = input()
    mod = 10**9 + 7
    a,b,c = 0,0,0
    for i in range(len(s)):
        if s[i] == 'A':
            a += pow(3,i,mod)
        elif s[i] == 'B':
            b += a
        elif s[i] == 'C':
            c += b
        else:
            c = 3*c + b
            b = 3*b + a
            a = 3*a + pow(3,i,mod)
        a %= mod
        b %= mod
        c %= mod
    print(c)
