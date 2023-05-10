def is_double_string(s):
    if len(s) % 2 == 1:
        return False
    else:
        n = len(s) // 2
        return s[:n] == s[n:]
