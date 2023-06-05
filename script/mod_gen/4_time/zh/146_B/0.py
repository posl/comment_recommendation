def move_char(ch, n):
    if not ch.isalpha():
        return ch
    if ch.isupper():
        offset = ord('A')
    else:
        offset = ord('a')
    return chr((ord(ch) - offset + n) % 26 + offset)

if __name__ == '__main__':
    move_char()