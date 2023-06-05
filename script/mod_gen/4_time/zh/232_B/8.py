def move_char(s, k):
    new_s = ''
    for i in range(len(s)):
        new_s += chr((ord(s[i]) - ord('a') + k) % 26 + ord('a'))
    return new_s

if __name__ == '__main__':
    move_char()