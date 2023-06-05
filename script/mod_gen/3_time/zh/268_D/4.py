def func(n, m, s, t):
    if n == 1 and m == 1:
        if s[0] == t[0]:
            return -1
        else:
            return s[0] + t[0]
    if n == 2 and m == 2:
        if s[0] == t[0] and s[1] == t[1]:
            return -1
        else:
            if s[0] == t[0]:
                return s[1] + t[1]
            elif s[1] == t[1]:
                return s[0] + t[0]
            else:
                return s[0] + t[0] + s[1] + t[1]
    if n == 3 and m == 3:
        if s[0] == t[0] and s[1] == t[1] and s[2] == t[2]:
            return -1
        else:
            if s[0] == t[0]:
                return s[1] + t[1] + s[2] + t[2]
            elif s[1] == t[1]:
                return s[0] + t[0] + s[2] + t[2]
            elif s[2] == t[2]:
                return s[0] + t[0] + s[1] + t[1]
            else:
                return s[0] + t[0] + s[1] + t[1] + s[2] + t[2]
    if n == 4 and m == 4:
        if s[0] == t[0] and s[1] == t[1] and s[2] == t[2] and s[3] == t[3]:
            return -1
        else:
            if s[0] == t[0]:
                return s[1] + t[1] + s[2] + t[2] + s[3] + t[3]
            elif s[1] == t[1]:
                return s[0] + t[0] + s[2] + t[2] + s[3] + t[3]
            elif s[2] == t[2]:
                return s

if __name__ == '__main__':
    func()