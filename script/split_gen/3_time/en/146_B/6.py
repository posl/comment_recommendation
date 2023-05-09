def shift(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i] != ' ':
            s[i] = chr(((ord(s[i]) - 65 + n) % 26) + 65)
    return ''.join(s)
