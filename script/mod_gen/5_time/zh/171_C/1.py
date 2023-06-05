def convert(n):
    if n <= 26:
        return chr(n + 96)
    else:
        return convert((n-1)//26) + chr((n-1)%26 + 97)

if __name__ == '__main__':
    convert()