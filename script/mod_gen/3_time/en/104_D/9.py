def abc(s):
    mod = 10**9+7
    s = s.replace('?','')
    l = len(s)
    if l < 3:
        return 0
    a = 0
    b = 0
    c = 0
    for i in range(l):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += a
        elif s[i] == 'C':
            c += b
    return c%mod
S = input()
print(abc(S))

if __name__ == '__main__':
    abc()