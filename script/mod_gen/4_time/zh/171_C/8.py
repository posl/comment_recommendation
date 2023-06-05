def convert(num):
    if num == 0:
        return ""
    elif num <= 26:
        return chr(96 + num)
    else:
        return convert((num - 1) // 26) + convert((num - 1) % 26 + 1)

if __name__ == '__main__':
    convert()