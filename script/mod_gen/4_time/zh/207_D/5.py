def is_match(s, t):
    s.sort()
    t.sort()
    for i in range(len(s)):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            return False
    return True

if __name__ == '__main__':
    is_match()