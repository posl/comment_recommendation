def move_letter(letter, n):
    letter = ord(letter) + n
    if letter > ord('Z'):
        letter = letter - ord('Z') + ord('A') - 1
    return chr(letter)

if __name__ == '__main__':
    move_letter()