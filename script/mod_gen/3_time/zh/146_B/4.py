def move_char(c, n):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        if ord(c) + n > ord('Z'):
            return chr(ord('A') + n - (ord('Z') - ord(c)) - 1)
        else:
            return chr(ord(c) + n)
    else:
        return c

if __name__ == '__main__':
    move_char()