def move_str(s, n):
    s = s.upper()
    n = n % 26
    res = ''
    for i in s:
        if ord(i) + n > ord('Z'):
            res += chr(ord(i) + n - ord('Z') + ord('A') - 1)
        else:
            res += chr(ord(i) + n)
    return res
