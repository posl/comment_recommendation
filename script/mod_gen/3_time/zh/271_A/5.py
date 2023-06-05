def convert_to_hex(num):
    hex_num = hex(num)
    return hex_num[2:].upper().zfill(2)

if __name__ == '__main__':
    convert_to_hex()