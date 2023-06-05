def rotate_string(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            return True
    return False

if __name__ == '__main__':
    rotate_string()