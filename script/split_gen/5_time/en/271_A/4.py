def convert_to_hexadecimal(num):
    return hex(num).upper()[2:].zfill(2)
print(convert_to_hexadecimal(int(input())))
