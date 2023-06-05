def move(s, n):
    if n == 0:
        return s
    else:
        s = list(s)
        for i in range(len(s)):
            s[i] = chr(ord(s[i]) + n)
            if ord(s[i]) > ord('Z'):
                s[i] = chr(ord(s[i]) - 26)
        return ''.join(s)
