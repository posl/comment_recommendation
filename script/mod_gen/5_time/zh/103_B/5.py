def rotateString(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False

if __name__ == '__main__':
    rotateString()