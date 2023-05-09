def get_alphabet(num):
    if num <= 26:
        return chr(96 + num)
    else:
        return get_alphabet(int((num - 1) / 26)) + chr(96 + num % 26)

if __name__ == '__main__':
    get_alphabet()