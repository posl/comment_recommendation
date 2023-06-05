def convert_to_hexadecimal(decimal):
    hexadecimal = hex(decimal)
    return hexadecimal[2:].upper()

if __name__ == '__main__':
    convert_to_hexadecimal()