def is_equal(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == t:
            return True
    return False

if __name__ == '__main__':
    is_equal()