def move(s, n):
    result = ''
    for c in s:
        if c.isupper():
            result += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            result += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        else:
            result += c
    return result
