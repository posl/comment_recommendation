def f(s):
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    if len(s) == 3:
        if s[0] == s[1] and s[0] == s[2]:
            return 1
        elif s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
            return 3
        else:
            return 6

if __name__ == '__main__':
    f()