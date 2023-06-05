def move(s, n):
    return chr((ord(s) - ord('A') + n) % 26 + ord('A'))
