def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False

if __name__ == '__main__':
    check()