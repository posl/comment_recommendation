def is_ok(s, m, base):
    if len(s) == 0:
        return 1
    n = int(s[0])
    if n == 0:
        return is_ok(s[1:], m, base)
    if n < base:
        return base ** (len(s) - 1)
    if n == base:
        return is_ok(s[1:], m, base) + int(s[1:], base) + 1
    if n > base:
        return int(base ** (len(s) - 1) + base ** (len(s) - 2)) * (n - 1) + is_ok(s[1:], m, base)
