def check(s):
    n = len(s)
    if n % 2 != 0:
        return False
    m = n // 2
    if s[:m] == s[m:]:
        return True
    return False

if __name__ == '__main__':
    check()