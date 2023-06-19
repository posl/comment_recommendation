def match(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] == '?':
            continue
        if s[i] != t[i]:
            return False
    return True

if __name__ == '__main__':
    match()