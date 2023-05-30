def abcnum(s):
    a = 0
    b = 0
    c = 0
    abc = 0
    q = 0
    for i in s:
        if i == 'A':
            a += 1
        elif i == 'B':
            b += 1
        elif i == 'C':
            c += 1
        elif i == '?':
            q += 1
    abc += a * b * q + a * c * b + b * c * a
    return (abc % (10**9 + 7))
s = input()
print(abcnum(s))
