def check(x):
    s = str(x)
    l = len(s)
    if l % 2 == 1:
        return False
    return s[:l//2] == s[l//2:]

if __name__ == '__main__':
    check()