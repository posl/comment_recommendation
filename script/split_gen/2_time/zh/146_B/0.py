def move_char(ch, n):
    if ch.islower():
        base = 'a'
    else:
        base = 'A'
    return chr((ord(ch) - ord(base) + n) % 26 + ord(base))
