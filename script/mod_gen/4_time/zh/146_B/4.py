def shift_char(char, n):
    # print("char: ", char)
    # print("n: ", n)
    # print("ord(char): ", ord(char))
    # print("ord(char) + n: ", ord(char) + n)
    # print("ord(char) + n - 65: ", ord(char) + n - 65)
    # print("(ord(char) + n - 65) % 26: ", (ord(char) + n - 65) % 26)
    # print("chr((ord(char) + n - 65) % 26 + 65): ", chr((ord(char) + n - 65) % 26 + 65))
    return chr((ord(char) + n - 65) % 26 + 65)

if __name__ == '__main__':
    shift_char()