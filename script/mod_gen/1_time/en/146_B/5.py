def shift_char(char, shift):
    if char.isalpha():
        if ord(char) + shift > ord('Z'):
            return chr(ord(char) + shift - 26)
        else:
            return chr(ord(char) + shift)
    else:
        return char

if __name__ == '__main__':
    shift_char()