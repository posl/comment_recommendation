def move_right(s, n):
    new_s = ''
    for c in s:
        new_s += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return new_s

if __name__ == '__main__':
    move_right()