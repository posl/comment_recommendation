def move(s, n):
    return chr((ord(s) - ord('A') + n) % 26 + ord('A'))

if __name__ == '__main__':
    move()