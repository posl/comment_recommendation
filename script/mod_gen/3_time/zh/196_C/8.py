def check(x):
    s = str(x)
    l = len(s)
    if l % 2 == 1:
        return False
    for i in range(l//2):
        if s[i] != s[i+l//2]:
            return False
    return True

if __name__ == '__main__':
    check()