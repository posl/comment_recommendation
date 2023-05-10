def get_next_letter(letter):
    letter = ord(letter)
    letter += 1
    return chr(letter)

if __name__ == '__main__':
    get_next_letter()