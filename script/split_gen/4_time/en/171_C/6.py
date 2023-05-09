def convert_to_alphabet(num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if num <= 26:
        return alphabet[num-1]
    else:
        return convert_to_alphabet((num-1)//26) + alphabet[(num-1)%26]
