def is_double(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    return s[:len(s)//2] == s[len(s)//2:]
