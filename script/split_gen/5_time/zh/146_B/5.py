def move_char(char, n):
    if ord(char) + n > ord('Z'):
        return chr(ord(char) + n - ord('Z') + ord('A') - 1)
    else:
        return chr(ord(char) + n)
