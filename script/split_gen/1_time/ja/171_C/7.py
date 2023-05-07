def convert_to_alphabet(num):
    if num == 0:
        return ''
    else:
        return convert_to_alphabet((num - 1) // 26) + chr((num - 1) % 26 + ord('a'))
