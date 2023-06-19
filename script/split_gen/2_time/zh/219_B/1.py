def get_s(s, t):
    s1 = ''
    for i in range(len(t)):
        if t[i] == '1':
            s1 += s[0]
        elif t[i] == '2':
            s1 += s[1]
        else:
            s1 += s[2]
    return s1
s1 = input()
s2 = input()
s3 = input()
t = input()
print(get_s(s1, t) + get_s(s2, t) + get_s(s3, t))
