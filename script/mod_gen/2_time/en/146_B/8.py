def shift_char(char, n):
    if char == " ":
        return char
    else:
        return chr((ord(char) - ord("A") + n) % 26 + ord("A"))

if __name__ == '__main__':
    shift_char()