def is_wonderful(s):
    if len(s) < 3:
        return False
    if s.islower():
        return False
    if s.isupper():
        return False
    if s.lower() == s.upper():
        return False
    for i in range(0, len(s)):
        if s[i].islower():
            if s[i].upper() not in s[i+1:]:
                return False
        if s[i].isupper():
            if s[i].lower() not in s[i+1:]:
                return False
    return True

if __name__ == '__main__':
    is_wonderful()