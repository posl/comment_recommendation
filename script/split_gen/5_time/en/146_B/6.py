def shift(s, n):
    s = s.upper()
    result = ""
    for c in s:
        if c.isalpha():
            if ord(c) + n > ord('Z'):
                result += chr(ord(c) + n - ord('Z') + ord('A') - 1)
            else:
                result += chr(ord(c) + n)
        else:
            result += c
    return result
