def move(s,n):
    s = s.upper()
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        if ord(s[i]) + n > 90:
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    s = ''.join(s)
    return s

if __name__ == '__main__':
    move()