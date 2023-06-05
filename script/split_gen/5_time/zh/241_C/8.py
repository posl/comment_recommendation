def is_ok(s):
    for i in range(len(s)):
        if s[i] == "#":
            return False
    return True
