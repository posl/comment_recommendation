def check(s, t):
    s = list(s)
    t = list(t)
    if s == t:
        return True
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s[i], s[j] = s[j], s[i]
            if s == t:
                return True
            s[i], s[j] = s[j], s[i]
    return False

if __name__ == '__main__':
    check()